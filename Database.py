import subprocess
import pandas as pd
import cryptography as cryp
import pickle
import datetime as dt

class AppInfo:
    def __init__(self, frame: pd.DataFrame):
        self.totalUptime = 0
        self.frame = frame

class DB:
    def __init__(self):
        self.appDict = {}

    def add(self, name: str):
        #Add checks to ensure name does not include a command injection
        df = pd.DataFrame(columns=["Date", "Uptime"])
        df.loc[len(df)] = [dt.date.today(), dt.time.min]
        appinfo = AppInfo(df)
        self.appDict[name] = appinfo
        print(self.appDict)
        print(df.values)



    def remove(self, name: str):
        if name in self.appDict.keys():
            self.appDict.pop(name)
        else:
            print("No such application exists in the dictionary, Something went wrong")