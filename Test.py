from Backtester import *


class Test(Backtester):

    def initialize(self):
        self.SetCashAmount(10000)
        self.SetStartDate(2, 21, 2021)
        self.SetEndDate(3, 17, 2021)
        self.AddEquity("AAPL", Resolution.Minute)

    def onData(self, candle):
        # Debug(candle)
        if not self.Portfolio.Invested:
            self.PlaceMarketOrder("AAPL", 10)
            Debug(self.Portfolio)



