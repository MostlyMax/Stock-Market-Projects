from ClientTDA import get_price_history
from datetime import datetime
import pandas as pd
from Algorithm import *
from Test import *


class Candle:
    def __init__(self, Symbol, High, Low, Open, Close, Datetime):
        self.Symbol = Symbol
        self.High = High
        self.Low = Low
        self.Open = Open
        self.Close = Close
        self.Datetime = Datetime


class Backtester:
    def __init__(self, algo):
        self.CurrentDatetime = 0
        self.CurrentTick = 0
        self.Data = {}
        self.CurrentData = {}
        self.CurrentCandle = {}
        self.Algo = algo
        self.run = True

    def GetNextTick(self):
        try:
            for ticker in self.Data:
                self.CurrentData[ticker] = self.Data[ticker].iloc[self.CurrentTick]
        except:
            self.run = False
        self.CurrentTick += 1

    def GetData(self):
        start = self.Algo.startDate
        end = self.Algo.endDate
        for security in self.Algo.Securities.values():
            resolution = security.Resolution
            ticker = security.Ticker
            self.Data[ticker] = get_price_history(symbol=ticker, start=start, end=end,
                                                  frequencyType=resolution["FrequencyType"],
                                                  periodType=resolution["PeriodType"],
                                                  frequency=resolution["Frequency"])

    def ProcessData(self):
        # print(self.CurrentData)
        for ticker in self.CurrentData:
            self.CurrentCandle[ticker] = Candle(Symbol=self.CurrentData[ticker].at['symbol'],
                                                High=self.CurrentData[ticker].at['high'],
                                                Low=self.CurrentData[ticker].at['low'],
                                                Open=self.CurrentData[ticker].at['open'],
                                                Close=self.CurrentData[ticker].at['close'],
                                                Datetime=datetime.fromtimestamp(
                                                    self.CurrentData[ticker].at['datetime'] / 1000))
            self.Algo.Securities[ticker].Price = self.CurrentCandle[ticker].Close

    def Update(self):
        self.GetNextTick()
        self.ProcessData()

    def Run(self):
        self.GetData()
        while self.Run:
            self.Update()
            Test2.onData(self.Algo, self.CurrentCandle)


if __name__ == '__main__':
    Algo = MAXAlgorithm()
    Test2.initialize(Algo)
    Backtester = Backtester(Algo)
    Backtester.Run()
