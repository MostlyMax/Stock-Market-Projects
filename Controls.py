from Portfolio import Portfolio
from Security import *


class Event:
    def CheckIfFilled(self, *args) -> bool:
        pass

    def Complete(self, *args):
        pass


class Order(Event):
    def __init__(self, Ticker, Price, Quantity, Type, Filled=False):
        self.Ticker = Ticker
        self.Price = Price
        self.Quantity = Quantity
        self.Filled = Filled
        self.Type = Type
        self.Cost = self.Price * self.Quantity

    def CheckIfFilled(self, Candles):
        Candle = Candles[self.Ticker]
        if Candle.High >= self.Price >= Candle.Low:
            return True
        else:
            return False

    def Complete(self, Algo):
        Algo.FillOrder(self)


class Controls:
    def __init__(self):
        self.Securities = {}
        self.Portfolio = Portfolio()
        self.Transactions = []
        self.Schedule = []

    def AddToSchedule(self, order):
        self.Schedule.append(order)

    def MarketOrder(self, ticker, Quantity):
        Price = self.Securities[ticker].Price
        order = Order(ticker, Price=Price, Quantity=Quantity, Type="MarketOrder")
        self.FillOrder(order)

    def LimitOrder(self, ticker, Quantity, Price):
        order = Order(ticker, Price=Price, Quantity=Quantity, Type="LimitOrder")
        self.AddToSchedule(order)

    def FillOrder(self, order):
        order.Filled = True
        self.Transactions.append(order)
        self.Portfolio.UpdateHolding(order)
        self.Portfolio.UpdatePortfolioValue()

    def CancelOrder(self, order):
        self.Schedule.remove(order)
