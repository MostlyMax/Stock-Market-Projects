class Portfolio:

    def __init__(self):
        self.CashAmount = 10000
        self.Invested = False
        self.EquityInvested = []

    def buyEquity(self, symbol, price, volume):
        self.EquityInvested.append(symbol, price, volume)
        self.Invested = True
        if self.CashAmount - price * volume < 0:
            raise Exception("Low Balance")
        else:
            self.CashAmount -= price * volume