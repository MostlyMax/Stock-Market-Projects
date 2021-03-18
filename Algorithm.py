from BacktestSettings import *
from Portfolio import *
from Backtester import *
from Test import *


class Algorithm:
    def __init__(self):
        self.Portfolio = Portfolio()
        self.Settings = BacktestSettings(self.Portfolio)

    def runAll(self):
        for equity in self.EquityList:
            backtest = Backtester()

            backtest.GetData(symbol=equity["Symbol"],
                             start=self.startDate, end=self.endDate,
                             resolution=equity["Resolution"])

            backtest.Run()


if __name__ == '__main__':
    algorithm = Algorithm()
    Test.initialize(algorithm.Settings)

    algorithm.runAll()


