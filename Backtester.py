from ClientTDA import get_price_history
from datetime import datetime
import pandas as pd
from Algorithm import *
from Test import *


class Candle:
    def __init__(self, Symbol, High=None, Low=None, Open=None, Close=None, Datetime=None, HasData=True):
        self.Symbol = Symbol
        self.High = High
        self.Low = Low
        self.Open = Open
        self.Close = Close
        self.Datetime = Datetime
        self.HasData = HasData


class Backtester:
    def __init__(self, algo):
        self.CurrentDatetime = 0
        self.CurrentTick = 0
        self.Data = {}
        self.CurrentData = {}
        self.CurrentCandle = {}
        self.Algo = algo
        self.CurrentDatetime = int(self.Algo.startDate.timestamp() * 1000)
        self.EndDatetime = int(self.Algo.endDate.timestamp() * 1000)

    def GetNextTick(self):
        for ticker in self.Data:
            try:
                self.CurrentData[ticker] = self.Data[ticker].loc[self.CurrentDatetime]
            except Exception:
                try:
                    self.CurrentData[ticker] = self.CurrentData[ticker]
                except Exception:
                    self.CurrentData[ticker] = None

        self.CurrentTick += 1
        self.CurrentDatetime += 60000

    def GetData(self):
        start = self.Algo.startDate
        end = self.Algo.endDate
        for security in self.Algo.Securities.values():
            resolution = security.Resolution
            ticker = security.Ticker
            self.Data[ticker] = get_price_history(symbol=ticker, start=start, end=end,
                                                  frequencyType=resolution["FrequencyType"],
                                                  periodType=resolution["PeriodType"],
                                                  frequency=resolution["Frequency"]).set_index("datetime")

    def ProcessData(self):
        # print(self.CurrentData)
        for ticker in self.CurrentData:
            if self.CurrentData[ticker] is None:
                self.CurrentCandle[ticker] = Candle(Symbol=ticker,
                                                    Datetime=datetime.fromtimestamp(self.CurrentDatetime / 1000),
                                                    HasData=False)
                continue

            self.CurrentCandle[ticker] = Candle(Symbol=ticker,
                                                High=self.CurrentData[ticker].at['high'],
                                                Low=self.CurrentData[ticker].at['low'],
                                                Open=self.CurrentData[ticker].at['open'],
                                                Close=self.CurrentData[ticker].at['close'],
                                                Datetime=datetime.fromtimestamp(self.CurrentDatetime / 1000))
            self.Algo.Securities[ticker].Price = self.CurrentCandle[ticker].Close
            try:
                self.Algo.Portfolio[ticker].UpdateSecurityHolding()
            except Exception:
                pass

    def Update(self):
        self.GetNextTick()
        self.ProcessData()
        Algo.Portfolio.UpdatePortfolioValue()

    def Run(self):
        self.GetData()
        while self.CurrentDatetime <= self.EndDatetime:
            self.Update()
            if all(data is None for data in self.CurrentCandle.values()):
                continue
            else: Test2.onData(self.Algo, self.CurrentCandle)


if __name__ == '__main__':
    Algo = MAXAlgorithm()
    Test2.initialize(Algo)
    Backtester = Backtester(Algo)
    Backtester.Run()
