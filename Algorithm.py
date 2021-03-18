from BacktestSystem import *
from Backtester import *


class Algorithm(Backtester, BacktestSystem, Portfolio):
    def __init__(self):
        Backtester.__init__(self)
        BacktestSystem.__init__(self)
        Portfolio.__init__(self)

