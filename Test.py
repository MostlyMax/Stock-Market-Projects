from Algorithm import *


class Test(Algorithm):
    # def __init__(self):
    #     super().__init__()

    def initialize(self):
        self.SetCashAmount(10)
        self.SetStartDate(3, 2, 2012)
        self.AddEquity("AAPL", Resolution.Hour)
        Debug(self.Portfolio.Invested)

    def onData(self, data):
        if not self.Portfolio.Invested:
            self.PlaceMarketOrder("AAPL", 10)
        pass



