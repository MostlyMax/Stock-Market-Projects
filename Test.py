from Example_Algorithm import *


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
            self.LimitOrder("AAPL", Quantity=3, Price=125)
        Debug(candle["AAPL"].Close)
        Debug(self.Portfolio.Holding["AAPL"])
