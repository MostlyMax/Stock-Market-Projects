from Portfolio import Portfolio
from Security import *


class Order:
    def __init__(self, Ticker, Price, Quantity, Type, Filled=False):
        self.Ticker = Ticker
        self.Price = Price
        self.Quantity = Quantity
        self.Filled = Filled
        self.Type = Type
        self.Cost = self.Price * self.Quantity


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

        # holding = SecurityHolding(order.Ticker, order.Quantity, order.Price)
        self.Portfolio[order.Ticker] = holding
        self.Portfolio.CashAmount -= order.Cost

    def CancelOrder(self, order):
        self.Schedule.remove(order)
