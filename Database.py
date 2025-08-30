import datetime
import pandas as pd
import datetime as dt

class AppInfo:
    def __init__(self, frame: pd.DataFrame):
        self.totalUptime = datetime.time.min
        self.frame = frame

class DB:
    def __init__(self):
        self.appDict = {}

    def add(self, name: str) -> int:
        #Add checks to ensure name does not include a command injection
        #Also add a persistent storage method for these dataframes
        if name not in self.appDict:
            df = pd.DataFrame(columns=["Date", "Uptime"])
            df.loc[len(df)] = [dt.date.today(), dt.time.min]
            appinfo = AppInfo(df)
            self.appDict[name] = appinfo
            print(self.appDict)
            print(df.values)
            return 0
        else:
            return 1


    def remove(self, name: str):
        if name in self.appDict.keys():
            self.appDict.pop(name)
        else:
            print("No such application exists in the dictionary, Something went wrong")