from AlgorithmInterface import *


class Example_Algorithm(Algorithm):

    def __init__(self, start):
        super().__init__(start)

        self.Tickers = ["AAPL"]
        self.StartingBalance = 100000

    def onData(self, candle):
        pass

    def initialize(self):
        pass
