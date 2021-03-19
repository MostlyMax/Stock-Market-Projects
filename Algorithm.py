from BacktestSettings import *
from Portfolio import *
from Backtester import *
from Test import *
import pandas as pd


class Algorithm:
    def __init__(self):
        self.Portfolio = Portfolio()
        self.Backtest = Backtester(self.Portfolio)

    def Run(self):
        self.Backtest.GetData(symbols=self.Backtest.EquityList,
                              start=self.Backtest.startDate,
                              end=self.Backtest.endDate)

        while self.Backtest.CurrentTick < len(self.Backtest.Data.index):
            self.Backtest.Update()
            Test.onData(self.Backtest, self.Backtest.CurrentCandle)


if __name__ == '__main__':
    algorithm = Algorithm()
    Test.initialize(algorithm.Backtest)

    algorithm.Run()
