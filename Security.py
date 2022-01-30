class Security:
    def __init__(self, Ticker, Resolution, extendedMarketHours, Price=None, HasData=True):
        self.Ticker = Ticker
        self.Price = Price
        self.Resolution = Resolution
        self.extendedMarketHours = extendedMarketHours
        self.Invested = False
        self.HasData = HasData


class SecurityHolding:
    def __init__(self, security, Quantity, Price):
        self.Security = security
        self.Quantity = Quantity
        self.UnrealizedProfit = 0
        self.Price = Price
        self.EntryPrice = Price

    def UpdateSecurityHolding(self):
        self.UnrealizedProfit = (self.Price - self.EntryPrice) * self.Quantity


