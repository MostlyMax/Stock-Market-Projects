from BacktestSystem import *
from Backtester import *


def Debug(*args):
    for x in args:
        print(x)


class Algorithm(Backtester, BacktestSystem, Portfolio):
    def __init__(self):
        Backtester.__init__(self)
        BacktestSystem.__init__(self)
        Portfolio.__init__(self)

    def run(self):
        for symbol in self.EquityList:
            self.GetData(symbol[0], self.startDate, self.endDate, symbol[1])
            Debug(self.Data)


