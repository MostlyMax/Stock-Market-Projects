from Backtester import *
from Algorithm import MAXAlgorithm


class Test():

    def initialize(self):
        self.SetCashAmount(10000)
        self.SetStartDate(2, 21, 2021)
        self.SetEndDate(3, 17, 2021)
        self.AddEquity("AAPL", Resolution.Minute)
        self.AddEquity("AMZN", Resolution.Minute)
        self.AddEquity("TSLA", Resolution.Minute)

    def onData(self, candle):
        # Debug(candle)
        if not self.Portfolio.Invested:
            self.PlaceMarketOrder("AAPL", 10)
            Debug(self.Portfolio)


class Test2(MAXAlgorithm):

    def initialize(self):
        self.SetCashAmount(100000)
        self.SetStartDate(2, 21, 2021)
        self.AddEquity("AAPL", Resolution.Minute)
        self.AddEquity("AMZN", Resolution.Minute)
        self.AddEquity("TSLA", Resolution.Minute)

    def onData(self, candle):
        if not self.Portfolio.Invested:
            print(candle["AAPL"].Close)
            print(candle["AMZN"].Close)
            print(candle["TSLA"].Close)
            self.MarketOrder("AAPL", 3)
            Debug(self.Portfolio)
