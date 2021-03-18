from BacktestSettings import *
from Backtester import *


class Test(BacktestSettings):

    def initialize(self):
        self.SetCashAmount(10)
        self.SetStartDate(2, 21, 2021)
        self.SetEndDate(3, 17, 2021)
        self.AddEquity("AAPL", Resolution.Day)

    def onData(self, candle):
        # Debug(candle)
        if not self.Portfolio.Invested:
            self.PlaceMarketOrder("AAPL", 10)
        pass



