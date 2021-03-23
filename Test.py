from Backtester import *
from Algorithm import MAXAlgorithm


class Test():

    def initialize(self):
        self.SetCashAmount(10000)
        self.SetStartDate(2, 21, 2021)
        self.SetEndDate(3, 17, 2021)
        self.AddEquity("AAPL", Resolution.Minute)
        self.AddEquity("AMZN", Resolution.Minute)
        self.AddEquity("TSLA", Resolution.Minute)

    def onData(self, candle):
        # Debug(candle)
        if not self.Portfolio.Invested:
            self.PlaceMarketOrder("AAPL", 10)
            Debug(self.Portfolio)


class Test2(MAXAlgorithm):

    def initialize(self):
        self.SetCashAmount(100000)
        self.SetStartDate(2, 21, 2021)
        self.AddEquity("AAPL", Resolution.Minute)
        self.AddEquity("AMZN", Resolution.Minute)
        self.AddEquity("TSLA", Resolution.Minute)

    def onData(self, candle):
        pass


class stuff1:
    def __init__(self):
        self.listofthings = []
        self.otherlistofthings = []

    def double_everything_in_list(self):
        for x in range(len(self.listofthings)):
            self.listofthings[x] = self.listofthings[x] * 2

class stuff2:
    def __init__(self):
        self.listofthings = []
        self.otherotherlistofthings = []

    def triple_everything_in_list(self):
        for x in range(len(self.listofthings)):
            self.listofthings[x] = self.listofthings[x] * 3

class stuffs(stuff1, stuff2):
    def __init__(self):
        stuff1.__init__(self)
        stuff2.__init__(self)
        self.listofthings = []

def teststuff():
    s = stuffs()
    s.listofthings.append(1)
    s.listofthings.append(2)
    s.listofthings.append(3)

    s.double_everything_in_list()
    print(s.listofthings)
    s.otherotherlistofthings.append(420)
    print(s.otherotherlistofthings)
    print(s.otherlistofthings)



if __name__ == '__main__':
    teststuff()
