from ClientTDA import get_price_history
from datetime import datetime
from BacktestSettings import *


class Candle:
    def __init__(self, High, Low, Open, Close, Datetime):
        self.High = High
        self.Low = Low
        self.Open = Open
        self.Close = Close
        self.Datetime = Datetime


class Backtester(BacktestSettings):
    def __init__(self, Portfolio):
        self.CurrentDatetime = 0
        self.CurrentTick = 0
        self.CurrentData = {}
        self.CurrentCandle = None
        self.Data = None
        self.Portfolio = Portfolio

    def PlaceMarketOrder(self, symbol, volume):
        price = self.CurrentCandle.Close
        self.Portfolio.buyEquity(symbol, price, volume)

    def GetNextTick(self):
        self.CurrentData = self.Data.iat[self.CurrentTick, 0]
        self.CurrentTick += 1

    def GetData(self, symbol, start, end, resolution):
        self.Data = get_price_history(symbol=symbol, start=start, end=end,
                                      frequencyType=resolution["FrequencyType"],
                                      periodType=resolution["PeriodType"],
                                      frequency=resolution["Frequency"])

    def ProcessData(self):
        self.CurrentCandle = Candle(High=self.CurrentData.get('high'),
                                    Low=self.CurrentData.get('low'),
                                    Open=self.CurrentData.get('open'),
                                    Close=self.CurrentData.get('close'),
                                    Datetime=datetime.fromtimestamp(self.CurrentData.get('datetime')/1000))

    def Update(self):
        self.GetNextTick()
        self.ProcessData()








