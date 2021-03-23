class Security:
    def __init__(self, Ticker, Resolution, extendedMarketHours, Price=0):
        self.Ticker = Ticker
        self.Price = Price
        self.Resolution = Resolution
        self.extendedMarketHours = extendedMarketHours


class SecurityHoldings:
    def __init__(self, security, Quantity=0):
        self.Security = security
        self.Quantity = Quantity
