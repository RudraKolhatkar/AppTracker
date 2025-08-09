import sys
import subprocess
from typing import List
from enum import Enum

from PySide6.QtGui import QBrush, QColor, QPen
from PySide6.QtCore import Qt
from PySide6.QtCharts import QChart, QChartView, QBarSet, QStackedBarSeries, QBarCategoryAxis, QValueAxis, QBarSeries
from PySide6.QtWidgets import QApplication, QMainWindow, QSplitter, QStackedWidget, QWidget, QHeaderView, QDialog, QListWidgetItem
import Dashboard
import AppDialog
import Database
import AddAppDialog


class AppData:
    def __init__(self, appName: str, data: list):
        self.appName = appName
        self.data = data

class chartType(Enum):
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"

class AddAppDialogWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = AddAppDialog.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.foundAppsList.itemDoubleClicked.connect(self.addApplicationList)
        self.ui.addButton.clicked.connect(self.addApplicationButt)
        self.ui.searchLineEdit.textChanged.connect(self.searchApps)

    def searchApps(self, text: str):
        self.ui.foundAppsList.clear()
        try:
            #Implement the command injection checker here
            terminalOutput = subprocess.check_output(f'pgrep -l {text}', shell=True, stderr=subprocess.STDOUT).decode('utf-8')
        except:
            return

        lines = terminalOutput.split("\n")

        for line in lines:
            self.ui.foundAppsList.addItem(line)

    def addApplicationList(self, item: QListWidgetItem):
        text = item.text().split()
        #Only two results are returned, we ignore the PID and use pass the name of the application
        db.add(text[1])

    def addApplicationButt(self):
        item = self.ui.foundAppsList.selectedItems()
        text = item[0].text().split()
        db.add(text[1])

class DashboardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Dashboard.Ui_Form()
        self.ui.setupUi(self)

        #Connect Add Application button to appropriate function
        self.ui.addButton.clicked.connect(self.popupAddAppDialog)

        #Adds a splitter
        self.ui.verticalLayout.removeWidget(self.ui.ChartFrame)
        self.ui.verticalLayout.removeWidget(self.ui.tableWidget)

        splitter = QSplitter(Qt.Orientation.Vertical)
        splitter.addWidget(self.ui.ChartFrame)
        splitter.addWidget(self.ui.tableWidget)
        splitter.setStretchFactor(0, 8)
        splitter.setStretchFactor(1, 1)

        self.ui.verticalLayout.addWidget(splitter)

        # #Add the stacked bar graph
        # #These become the separate applications
        # set0 = QBarSet("Label 1")
        # set1 = QBarSet("Label 2")
        # set2 = QBarSet("Label 3")
        # set3 = QBarSet("Label 4")
        # set4 = QBarSet("Label 5")
        #
        #
        # #These become the values for all the applications in order of the sets created
        # set0 << 1 << 2 << 3
        # set0 << 4 << 5 << 6 << 1
        # set1 << 4 << 2 << 2 << 4 << 7 << 2 << 2
        # set2 << 2 << 1 << 6 << 4 << 5 << 3 << 3
        # set3 << 6 << 13 << 3 << 7 << 5 << 5 << 4
        # set4 << 9 << 21 << 3 << 4 << 8 << 7 << 5
        #
        # series = QStackedBarSeries()
        # series.append(set0)
        # series.append(set1)
        # series.append(set2)
        # series.append(set3)
        # series.append(set4)
        # series.hovered.connect(self.barsetOnHover)
        #
        # chart = QChart()
        # chart.addSeries(series)
        # chart.setTitle("Example")
        # chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        # chart.setBackgroundBrush(QBrush(QColor("#2F2E34")))
        # chart.setBackgroundVisible(True)
        # chart.setTitleBrush(QBrush(QColor("white")))
        # chart.legend().setLabelBrush(QBrush(QColor("white")))
        #
        # #These will be the dates/months/years
        # categories = ["first", "second", "Third", "Fourth", "Fifth", "Sixth", "Seven"]
        #
        # axisY = QBarCategoryAxis()
        # axisY.append(categories)
        # axisY.setLabelsBrush(QBrush(QColor("white")))
        # axisY.setGridLineVisible(False)
        # chart.addAxis(axisY, Qt.AlignmentFlag.AlignBottom)
        # series.attachAxis(axisY)
        #
        # axisX = QValueAxis()
        # axisX.setLabelsBrush(QBrush(QColor("white")))
        # axisX.setGridLineVisible(False)
        # axisX.setRange(0, 50)
        # chart.addAxis(axisX, Qt.AlignmentFlag.AlignLeft)
        # series.attachAxis(axisX)
        #
        # weekChartView = QChartView(chart)
        # chartSwitcher = QStackedWidget()
        # chartSwitcher.addWidget(weekChartView)
        # self.ui.verticalLayout_2.addWidget(chartSwitcher)



        #Modifications to the table
        self.ui.tableWidget.setColumnWidth(0, 1200)
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)


    def popupAddAppDialog(self):
        diag = AddAppDialogWidget()
        diag.exec()

    def createChart(self, appData: List[AppData], categories: List[str], type: chartType) -> QChartView:
        barsets: List[QBarSet] = []

        for app in appData:
            barsets.append(QBarSet(app.appName))
            for uptime in app.data:
                barsets[-1] << uptime

        series = QStackedBarSeries()
        for set in barsets:
            series.append(set)

        series.hovered.connect(self.barsetOnHover)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle(type.value)
        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        chart.setBackgroundBrush(QBrush(QColor("#2F2E34")))
        chart.setBackgroundVisible(True)
        chart.setTitleBrush(QBrush(QColor("white")))
        chart.legend().setLabelBrush(QBrush(QColor("white")))

        axisY = QBarCategoryAxis()
        axisY.append(categories)
        axisY.setLabelsBrush(QBrush(QColor("white")))
        axisY.setGridLineVisible(False)
        chart.addAxis(axisY, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(axisY)

        axisX = QValueAxis()
        axisX.setLabelsBrush(QBrush(QColor("white")))
        axisX.setGridLineVisible(False)
        axisX.setRange(0, 50)
        chart.addAxis(axisX, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axisX)

        #Switching to App history view
        series.clicked.connect(self.barsetClicked)

        return QChartView(chart)

    def barsetClicked(self, index, barset: QBarSet):
        win.setCurrentWidget(appDialog)
        print(barset.label())

    def barsetOnHover(self, status: bool, index: int, barset: QBarSet):
        if status:
            pen = QPen(QColor("white"))
            pen.setWidth(4)
            barset.setPen(pen)

        else:
            pen = QPen(QColor("white"))
            pen.setWidth(1)
            barset.setPen(pen)


class AppDialogWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = AppDialog.Ui_Form()
        self.ui.setupUi(self)

        #Adds a splitter
        self.ui.verticalLayout.removeWidget(self.ui.frame)
        self.ui.verticalLayout.removeWidget(self.ui.tableWidget)

        splitter = QSplitter(Qt.Orientation.Vertical)
        splitter.addWidget(self.ui.frame)
        splitter.addWidget(self.ui.tableWidget)
        splitter.setStretchFactor(0, 8)
        splitter.setStretchFactor(1, 1)

        self.ui.verticalLayout.addWidget(splitter)

        #Create and Modify the BarChart
        #This will be the name of the Application and the data of each day in the week
        set0 = QBarSet("Label 1")
        set0 << 1 << 2 << 3 << 4 << 5 << 6 << 7

        series = QBarSeries()
        series.append(set0)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Application History")
        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        chart.setBackgroundBrush(QBrush(QColor("#2F2E34")))
        chart.legend().setLabelBrush(QBrush(QColor("white")))
        chart.setTitleBrush(QBrush(QColor("white")))

        categories = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh"]
        axisX = QBarCategoryAxis()
        axisX.append(categories)
        axisX.setGridLineVisible(False)
        axisX.setLabelsBrush(QBrush(QColor("white")))
        chart.addAxis(axisX, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(axisX)

        axisY = QValueAxis()
        axisY.setRange(0, 8)
        axisY.setGridLineVisible(False)
        axisY.setLabelsBrush(QBrush(QColor("white")))
        chart.addAxis(axisY, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axisY)

        chartview = QChartView(chart)
        self.ui.verticalLayout_2.addWidget(chartview)

        #modify the table attributes
        self.ui.tableWidget.setColumnWidth(0, 1200)
        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)

        #Connect the Dashboard button
        self.ui.dashboardButton.clicked.connect(self.dashboardClicked)

    def dashboardClicked(self):
        win.setCurrentWidget(dashboard)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = Database.DB()

    win = QStackedWidget()
    dashboard = DashboardWidget()
    appDialog = AppDialogWidget()
    win.addWidget(dashboard)
    win.addWidget(appDialog)
    win.resize(1400, 900)
    win.setStyleSheet("background-color: rgb(47, 46, 52);")

    win.show()
    app.exec()