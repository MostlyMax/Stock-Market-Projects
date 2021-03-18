from ClientTDA import get_price_history

class Bar:
    def __init__(self, High, Low, Open, Close):
        self.High = High
        self.Low = Low
        self.Open = Open
        self.Close = Close


class Portfolio:

    def __init__(self):
        self.Portfolio = self
        self.CashAmount = 10000
        self.Invested = False
        self.EquityInvested = []

    def SetCashAmount(self, amount):
        self.CashAmount = amount

    def buyEquity(self, symbol, price, volume):
        self.EquityInvested.append(symbol, price, volume)
        self.Invested = True
        if self.CashAmount - price * volume < 0:
            raise Exception("Low Balance")
        else:
            self.CashAmount -= price * volume


class Backtester:
    def __init__(self):
        self.CurrentDatetime = 0
        self.CurrentTick = 0
        self.CurrentData = {}
        self.Data = None

    def PlaceMarketOrder(self, symbol, volume):
        currentData = self.CurrentData.get(symbol)
        price = currentData.Close
        Portfolio.buyEquity(symbol, price, volume)

    def GetNextTick(self):
        pass

    def GetData(self, symbol, start, end, resolution):
        self.Data = get_price_history(symbol, start, end, resolution)

    def ProcessData(self):
        pass





