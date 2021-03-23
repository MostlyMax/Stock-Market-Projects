from Environment import *
from Security import Security
from Order import *
import pandas as pd


class MAXAlgorithm(Environment):
    def __init__(self):
        self.Securities = {}
        self.Portfolio = {}
        self.Transactions = None
        self.Schedule = None
        Environment.__init__(self)

    def AddEquity(self, ticker, resolution=Resolution.Minute, extendedMarketHours=False):
        self.Securities[ticker] = Security(ticker, resolution, extendedMarketHours)

    def onData(self, candle):
        pass

    def initialize(self):
        pass

    def PlaceMarketOrder(self):
        pass

    def PlaceLimitOrder(self):
        pass

    # def __init__(self):
    #     self.Portfolio = Portfolio()
    #     self.Backtest = Backtester(self.Portfolio)

    # def Run(self):
    #     self.Backtest.GetData(symbols=self.Backtest.EquityList,
    #                           start=self.Backtest.startDate,
    #                           end=self.Backtest.endDate)
    #
    #     while self.Backtest.CurrentTick < len(self.Backtest.Data.index):
    #         self.Backtest.Update()
    #         Test.onData(self.Backtest, self.Backtest.CurrentCandle)
