import pandas as pd
from Security import SecurityHolding

class Portfolio:

    def __init__(self):
        self.Holding = {}
        self.CashAmount = 100000
        self.Invested = False
        self.TotalValue = 100000

    def __getitem__(self, item):
        return self.Holding[item]

    def __setitem__(self, key, value):
        self.Holding[key] = value

    def UpdateHolding(self, FilledOrder):
        if FilledOrder.Ticker in self.Holding:
            self.UpdatePosition(FilledOrder)
        else:
            self.OpenPosition(FilledOrder)

        self.CashAmount -= FilledOrder.Cost

    def OpenPosition(self, FilledOrder):
        holding = SecurityHolding(FilledOrder.Ticker, FilledOrder.Quantity, FilledOrder.Price)
        self.Holding[FilledOrder.Ticker] = holding

    # This is probably the messiest code in this project
    # Couldn't think of a better way of doing this thoug...
    def UpdatePosition(self, FilledOrder):
        holding = self.Holding[FilledOrder.Ticker]

        # If the order just closes your position, delete it from holding
        if holding.Quantity + FilledOrder.Quantity == 0:
            self.Holding.pop(FilledOrder.Ticker)

        # If the order grows your position, average the price and combine the quantity
        elif holding.Quantity * FilledOrder.Quantity > 0:
            holding.Price = (holding.Price * holding.Quantity + FilledOrder.Price * FilledOrder.Quantity)\
                            / (holding.Quantity + FilledOrder.Quantity)
            holding.Quantity += FilledOrder.Quantity

        # If the order closes shrinks your position...
        elif holding.Quantity * FilledOrder.Quantity < 0:
            # If it doesn't close it, just subtract the quantity
            if abs(holding.Quantity) > abs(FilledOrder.Quantity):
                holding.Quantity += FilledOrder.Quantity
            # If it closes it, close old position and open a new one with
            # subtracted quantity and new price
            if abs(holding.Quantity) < abs(FilledOrder.Quantity):
                newQuantity = FilledOrder.Quantity + holding.Quantity
                holding = SecurityHolding(FilledOrder.Ticker, newQuantity, FilledOrder.Price)
                self.Holding[FilledOrder.Ticker] = holding

    def UpdatePortfolioValue(self):
        self.TotalValue = self.CashAmount
        for security in self.Holding:
            self.TotalValue += security.UnrealizedProfit


