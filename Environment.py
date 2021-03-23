from datetime import datetime
from datetime import timedelta
from tda.client import Client
from pprint import pprint
from Security import Security
from Portfolio import Portfolio


def Debug(*args):
    for x in args:
        try:
            pprint(vars(x))
        except:
            pprint(x)


class Resolution:
    Minute = {"FrequencyType": Client.PriceHistory.FrequencyType.MINUTE,
              "Frequency": Client.PriceHistory.Frequency.EVERY_MINUTE,
              "PeriodType": Client.PriceHistory.PeriodType.DAY}

    Day = {"FrequencyType": Client.PriceHistory.FrequencyType.DAILY,
           "Frequency": Client.PriceHistory.Frequency.DAILY,
           "PeriodType": Client.PriceHistory.PeriodType.MONTH}

    HalfHour = {"FrequencyType": Client.PriceHistory.FrequencyType.MINUTE,
                "Frequency": Client.PriceHistory.Frequency.EVERY_THIRTY_MINUTES,
                "PeriodType": Client.PriceHistory.PeriodType.DAY}


class Environment:

    def __init__(self):
        self.InitialCashAmount = 100000
        self.status = 0
        self.startDate = datetime.today() - timedelta(days=2)
        self.endDate = datetime.today() - timedelta(days=1)

        self.Securities = {}
        self.Portfolio = Portfolio()
        self.Transactions = []
        self.Schedule = []

    def SetStartDate(self, month, day, year):
        self.startDate = datetime(year=year, month=month, day=day)

    def SetEndDate(self, month, day, year):
        self.endDate = datetime(year=year, month=month, day=day)

    def SetCashAmount(self, amount):
        self.InitialCashAmount = amount
        self.Portfolio.CashAmount = amount

    def AddEquity(self, ticker, resolution=Resolution.Minute, extendedMarketHours=False):
        self.Securities[ticker] = Security(ticker, resolution, extendedMarketHours)



