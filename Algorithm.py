from BacktestSettings import *
from Portfolio import *
from Backtester import *
from Test import *


class Algorithm:
    def __init__(self):
        self.Portfolio = Portfolio()
        self.Settings = BacktestSettings(self.Portfolio)

    def RunAll(self):
        for equity in self.Settings.EquityList:
            backtest = Backtester(self.Portfolio)

            backtest.GetData(symbol=equity["Symbol"],
                             start=self.Settings.startDate,
                             end=self.Settings.endDate,
                             resolution=equity["Resolution"])
            self.Run(backtest)

    def Run(self, backtest):
        while backtest.CurrentTick < len(backtest.Data.index):
            backtest.Update()
            Test.onData(self.Settings, backtest.CurrentCandle)


if __name__ == '__main__':
    algorithm = Algorithm()
    Test.initialize(algorithm.Settings)

    algorithm.RunAll()


