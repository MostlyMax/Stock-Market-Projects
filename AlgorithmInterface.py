import pandas as pd
import matplotlib.pyplot as plt
import traceback
import argparse
import numpy as np
import logging
from Environment import *

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger('Backtester.py')
logger.setLevel(level=logging.DEBUG)


class Resolution:
    Minute = {"FrequencyType": Client.PriceHistory.FrequencyType.MINUTE,
              "Frequency": Client.PriceHistory.Frequency.EVERY_MINUTE,
              "PeriodType": Client.PriceHistory.PeriodType.DAY}

    Day = {"FrequencyType": Client.PriceHistory.FrequencyType.DAILY,
           "Frequency": Client.PriceHistory.Frequency.DAILY,
           "PeriodType": Client.PriceHistory.PeriodType.MONTH}

    HalfHour = {"FrequencyType": Client.PriceHistory.FrequencyType.MINUTE,
                "Frequency": Client.PriceHistory.Frequency.EVERY_THIRTY_MINUTES,
                "PeriodType": Client.PriceHistory.PeriodType.DAY}


class Order:
    SHORT = 'SHORT'
    BUY = 'BUY'
    SELL = 'SELL'

    def __init__(self, order_type, ticker, price, volume, date=None):
        self.order_type = order_type
        self.ticker = ticker
        self.price = price
        if order_type == Order.BUY: self.volume = abs(volume)
        if order_type == Order.SHORT: self.volume = -abs(volume)
        if order_type == Order.SELL: self.volume = -abs(volume)
        self.date = date


class Wallet:
    def __init__(self, start, Balance=100000):

        self.Starting_Balance = Balance
        self.Balance = Balance
        self.Portfolio_Value = Balance

        self.TradeLog = []  # pd.DataFrame(columns=['Type', 'Ticker', 'Price', 'Volume', 'Datetime'])
        self.TradeLogColumns = ['Type', 'Ticker', 'Price', 'Volume', 'Datetime']
        self.CurrentPositions = {}

        self.IN_TRADE_TICKER_LONG = []
        self.IN_TRADE_TICKER_SHORT = []
        self.IN_TRADE = False

        self.Track_Portfolio_Value = [{'date': start, 'value': self.Portfolio_Value, 'balance': self.Balance}]

        self.now = None

    def UpdateData(self, currentSlice):
        self.Portfolio_Value = self.Balance
        for ticker, pos in self.CurrentPositions.items():
            self.Portfolio_Value += currentSlice[ticker].close * pos['volume']

        self.Track_Portfolio_Value.append({'date': self.now, 'value': self.Portfolio_Value, 'balance': self.Balance})

        if self.CurrentPositions:
            self.IN_TRADE = True
        else:
            self.IN_TRADE = False

    def PlaceOrder(self, order: Order):
        self.Balance -= order.price * order.volume

        self.TradeLog.append(order)

        if order.ticker in self.CurrentPositions:
            ticker_position = self.CurrentPositions[order.ticker]

            prev_cost = ticker_position['avg_price'] * ticker_position['volume']
            new_cost = prev_cost + order.price * order.volume
            ticker_position['volume'] += order.volume

            if ticker_position['volume'] == 0:
                del self.CurrentPositions[order.ticker]
                return

            avg_price = (prev_cost + new_cost) / (ticker_position['volume'])
            ticker_position['avg_price'] = avg_price

        else:
            self.CurrentPositions[order.ticker] = {'volume': order.volume, 'avg_price': order.price}

    def ClosePosition(self, ticker, currentSlice):
        position = self.CurrentPositions.get(ticker, None)

        if position is None:
            logger.warning("Tried to close position that did not exist!")
            return

        current_price = currentSlice[ticker].close

        if position['volume'] > 0:
            order_type = Order.SELL
        else:
            order_type = Order.BUY

        self.PlaceOrder(Order(order_type, ticker, current_price, position['volume'], self.now))

    def CloseAllPositions(self, currentSlice):
        tickers = list(self.CurrentPositions.keys())

        for ticker in tickers:
            self.ClosePosition(ticker, currentSlice)

    def PlotData(self, Market):
        balance_df = pd.DataFrame(self.Track_Portfolio_Value)

        balance_df['log_balance'] = np.log(balance_df['value'])
        Market['Rolling_pChange'] = Market['pChange'].rolling(len(Market.index), min_periods=1).apply(np.prod)
        Market['Balance'] = self.Starting_Balance * Market['Rolling_pChange']
        Market['log_balance'] = np.log(Market['Balance'])

        fig, ax1 = plt.subplots()

        ax1.plot(balance_df.date, balance_df.log_balance, c='green', label='Algorithm')
        ax1.plot(Market.index, Market.log_balance, c='blue', label='Market>')

        plt.legend()
        plt.show()


class Algorithm:
    def __init__(self, start):
        self.Tickers = []
        self.StartingBalance = 100000
        self.WarmupPeriod = 0
        self.Resolution = Resolution.Day

        self.tickerData = {}
        self.currentSlice = {}
        self.now = None
        self.wallet = Wallet(start, self.StartingBalance)

    def OnData(self):
        pass

    def OnFinish(self, market):
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--Update", action='store_true', help="Update CSV Files")
    args = parser.parse_args()

    Backtester.main(args.Update, Algorithm,
                    start=datetime(month=1, day=1, year=2014),
                    end=datetime(month=12, day=31, year=2018))
