from BacktestSettings import *
from Portfolio import *
from Backtester import *
from Test import *
import pandas as pd


class Algorithm:
    def __init__(self):
        self.Portfolio = Portfolio()
        self.Backtest = Backtester(self.Portfolio)

    def RunAll(self):
        self.Backtest.GetData(symbols=self.Backtest.EquityList,
                              start=self.Backtest.startDate,
                              end=self.Backtest.endDate)
        self.Run(self.Backtest)

    def Run(self, backtest):
        while backtest.CurrentTick < len(backtest.Data.index):
            backtest.Update()
            Test.onData(backtest, backtest.CurrentCandle)


if __name__ == '__main__':
    algorithm = Algorithm()
    Test.initialize(algorithm.Backtest)

    algorithm.RunAll()
