import pandas as pd


class Portfolio:

    def __init__(self):
        self.Tickers = {}
        self.CashAmount = 100000
        self.Invested = False
        self.TotalValue = 100000

    def __getitem__(self, item):
        return self.Tickers[item]

    def __setitem__(self, key, value):
        self.Tickers[key] = value

    def UpdatePortfolioValue(self):
        self.TotalValue = self.CashAmount
        for SecurityHolding in self.Tickers:
            self.TotalValue += SecurityHolding.UnrealizedProfit


