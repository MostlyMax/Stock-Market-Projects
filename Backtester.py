from ClientTDA import get_price_history
from datetime import datetime
from BacktestSettings import *
import pandas as pd


class Candle:
    def __init__(self, Symbol, High, Low, Open, Close, Datetime):
        self.Symbol = Symbol
        self.High = High
        self.Low = Low
        self.Open = Open
        self.Close = Close
        self.Datetime = Datetime


class Backtester(BacktestSettings):
    def __init__(self, Portfolio):
        super().__init__(Portfolio)
        self.CurrentDatetime = 0
        self.CurrentTick = 0
        self.CurrentData = {}
        self.CurrentCandle = None
        self.Data = pd.DataFrame(columns=["open", "high", "low", "close", "datetime", "symbol"])

    def PlaceMarketOrder(self, symbol, volume):
        price = self.CurrentCandle.Close
        self.Portfolio.buyEquity(symbol, price, volume)

    def GetNextTick(self):
        self.CurrentData = self.Data.iloc[self.CurrentTick]
        self.CurrentTick += 1

    def GetData(self, symbols, start, end):
        for symbol in symbols:
            resolution = symbol["Resolution"]
            tempData = get_price_history(symbol=symbol["Symbol"], start=start, end=end,
                                          frequencyType=resolution["FrequencyType"],
                                          periodType=resolution["PeriodType"],
                                          frequency=resolution["Frequency"])
            self.Data = pd.concat([self.Data, tempData])
            self.Data.dropna(subset=["datetime"], inplace=True)
            self.Data.sort_values(by=["datetime"], inplace=True)
            print(self.Data)

    def ProcessData(self):
        # print(self.CurrentData)
        self.CurrentCandle = Candle(Symbol=self.CurrentData.at['symbol'],
                                    High=self.CurrentData.at['high'],
                                    Low=self.CurrentData.at['low'],
                                    Open=self.CurrentData.at['open'],
                                    Close=self.CurrentData.at['close'],
                                    Datetime=datetime.fromtimestamp(self.CurrentData.at['datetime']/1000))

    def Update(self):
        self.GetNextTick()
        self.ProcessData()









