from datetime import datetime


class Resolution:
    Minute = "minute"
    Hour = "hour"
    Day = "day"


def Debug(*args):
    for x in args:
        print(x)


class BacktestSystem:

    def __init__(self):
        self.status = 0
        self.equityList = []
        self.startDate = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        self.endDate = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    def SetStartDate(self, month, day, year):
        self.startDate = datetime(year=year, month=month, day=day)

    def SetEndDate(self, month, day, year):
        self.endDate = datetime(year=year, month=month, day=day)

    def AddEquity(self, symbol, resolution=Resolution.Minute, *args):
        self.equityList.append([symbol, resolution, args])




