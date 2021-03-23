import pandas as pd


class Portfolio:

    def __init__(self, CashAmount):
        self.CashAmount = CashAmount
        self.Invested = False
        self.EquityInvested = pd.DataFrame(index=["Symbol"], columns=["Current Price", "Volume"])
        self.PortfolioValue = 10000

    def EquityOrder(self, symbol, price, volume):
        print(self.EquityInvested)
        self.EquityInvested.at[symbol, "Volume"] += volume
        self.EquityInvested.at[symbol, "Current Price"] = price

        if self.CashAmount - price * volume < 0:
            raise Exception("Low Balance")
        else:
            self.CashAmount -= price * volume

    def UpdatePortfolioValue(self):
        self.PortfolioValue = self.CashAmount

        for equity in self.EquityInvested.index:
            print(equity)
            price = self.EquityInvested.at[equity, "Current Price"]
            volume = self.EquityInvested.at[equity, "Volume"]
            self.PortfolioValue += price * volume

        print(self.PortfolioValue)

    def UpdatePortfolio(self, candle):
        if self.EquityInvested["Volume"].sum() != 0:
            self.Invested = True
        else:
            self.Invested = False

        self.EquityInvested.at[candle.Symbol, "Current Price"] = candle.Close

        self.UpdatePortfolioValue()
