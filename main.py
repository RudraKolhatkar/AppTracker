import datetime
import sys
import subprocess
import threading
import time
import pickle
from typing import List
from enum import Enum

from PySide6.QtGui import QBrush, QColor, QPen, QAction, QIcon
from PySide6.QtCore import Qt
from PySide6.QtCharts import QChart, QChartView, QBarSet, QStackedBarSeries, QBarCategoryAxis, QValueAxis, QBarSeries
from PySide6.QtWidgets import QApplication, QMainWindow, QSplitter, QStackedWidget, QWidget, QHeaderView, QDialog, \
    QListWidgetItem, QMessageBox, QSystemTrayIcon, QMenu, QTableWidgetItem
import Dashboard
import AppDialog
import Database
import AddAppDialog
from Database import AppInfo

mutex = threading.Lock()


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
            terminalOutput = subprocess.check_output(f'pgrep -l {text}', shell=True, stderr=subprocess.STDOUT).decode(
                'utf-8')
        except:
            return

        lines = terminalOutput.split("\n")

        for line in lines:
            self.ui.foundAppsList.addItem(line)

    def addApplicationList(self, item: QListWidgetItem):
        text = item.text().split()
        #Only two results are returned, we ignore the PID and pass the name of the application
        if db.add(text[1]) == 1:
            alert = QMessageBox.information(self, "Item Exists",
                                            "The item you have selected is already in the Database")

    def addApplicationButt(self):
        item = self.ui.foundAppsList.selectedItems()
        text = item[0].text().split()
        if db.add(text[1]) == 1:
            alert = QMessageBox.information(self, "Item Exists",
                                            "The item you have selected is already in the Database")


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
        self.ui.tableWidget.setColumnWidth(0, 1250)
        rowcount = 0
        for name in db.appDict.keys():
            self.ui.tableWidget.insertRow(rowcount)

            self.ui.tableWidget.setItem(rowcount, 0, QTableWidgetItem(name))
            uptime = db.appDict[name].totalUptime.strftime("%H:%M:%S")
            self.ui.tableWidget.setItem(rowcount, 1, QTableWidgetItem(uptime))

            rowcount += 1

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


def daemonThread(DB: Database.DB):
    while True:
        for value in DB.appDict.values():
            with mutex:
                value.totalUptime = addSecs(value.totalUptime, 1)

                #Get all indices that have the date of today
                indices = value.frame.index[value.frame["Date"] == datetime.date.today()].tolist()
                if indices:
                    row = value.frame.loc[indices[-1]]
                    newTime = addSecs(row["Uptime"], 1)
                    value.frame.loc[indices[-1], "Uptime"] = newTime
                else:
                    value.frame.loc[len(value.frame)] = [datetime.date.today(), datetime.time.min]

            print(value.frame)

        file = open("DB pickle", "wb")
        pickle.dump(DB, file)
        file.close()

        time.sleep(1)


def addSecs(tm: datetime.time, secs) -> datetime.time:
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    icon = QIcon("icon.png")
    tray = QSystemTrayIcon(icon)
    tray.setVisible(True)

    menu = QMenu()
    quitAction = QAction("Quit")
    quitAction.triggered.connect(app.quit)
    menu.addAction(quitAction)
    tray.setContextMenu(menu)

    try:
        dbFile = open("DB pickle", "rb")
        db = pickle.load(dbFile)
        dbFile.close()
    except FileNotFoundError:
        db = Database.DB()

    daemon = threading.Thread(target=daemonThread, name='daemon', args=(db,))
    daemon.daemon = True
    daemon.start()

    win = QStackedWidget()
    dashboard = DashboardWidget()
    appDialog = AppDialogWidget()
    win.addWidget(dashboard)
    win.addWidget(appDialog)
    win.resize(1400, 900)
    win.setStyleSheet("background-color: rgb(47, 46, 52);")

    win.show()
    app.exec()
