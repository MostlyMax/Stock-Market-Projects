from Environment import *
from Controls import *


class MAXAlgorithm(Environment, Controls):

    def __init__(self):
        self.Securities = {}
        self.Portfolio = Portfolio()
        self.Transactions = []
        self.Schedule = []
        Environment.__init__(self)
        Controls.__init__(self)

    def onData(self, candle):
        pass

    def initialize(self):
        pass
