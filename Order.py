
class Order:
    def __init__(self, Ticker, Price, Quantity=1, Filled=False):
        self.Ticker = Ticker
        self.Price = Price
        self.Quantity = Quantity
        self.Filled = Filled


class MarketOrder(Order):
    def __init__(self, Ticker, Price):
        super.__init__(Ticker, Price, Filled=True)


class LimitOrder(Order):
    def __init__(self):
        pass