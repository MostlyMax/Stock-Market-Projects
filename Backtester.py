from termcolor import colored
import tdaClientInterpreter as tda
from datetime import datetime, timedelta
import traceback
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tqdm import tqdm
import logging
from AlgorithmInterface import Algorithm, Wallet


logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger('Backtester.py')
logger.setLevel(level=logging.DEBUG)


class Backtester:
    def __init__(self, start, end, tickers):
        self.tickers = tickers

        self.Market = pd.read_csv("Resources/Data/SPY_daily_data.csv", index_col=0,
                                  parse_dates=['datetime'])

        self.startDatetime = start
        self.endDatetime = end

        self.tickerData = {}
        for ticker in self.tickers:
            try:
                self.tickerData[ticker] = pd.read_csv(f"Resources/Data/{ticker}_daily_data.csv", index_col=0,
                                                      parse_dates=['datetime'])
            except FileNotFoundError:
                self.tickers.remove(ticker)

        # Init Variables:
        self.WarmUp = 0

    def PreProcess(self):
        self.Market['pChange'] = self.Market['close'] / self.Market['close'].shift(1)

        for ticker, data in self.tickerData.items():
            data['pChange_ratio'] = data['close'] / data['close'].shift(1)
            data['pChange'] = 1 - data['pChange_ratio']

            data.dropna(inplace=True)

    def RunBacktest(self, algo: Algorithm):
        delta_day = timedelta(days=1)
        delta_hour = timedelta(hours=1)

        idxCount = 0
        for idx, row in tqdm(self.Market.iterrows(), total=len(self.Market.index)):
            idx = idx + delta_hour

            if idxCount <= self.WarmUp:
                idxCount += 1
                continue

            for ticker, data in self.tickerData.items():
                # Not all
                for hr_adjust in range(0, 4):
                    if idx - (hr_adjust * delta_hour) in data.index:
                        algo.tickerData[ticker] = data.loc[:idx - (hr_adjust * delta_hour)]

                        currentSlice = data.loc[idx - (hr_adjust * delta_hour)]
                        algo.currentSlice[ticker] = currentSlice
                        break
                else:
                    algo.currentSlice[ticker] = None

            algo.now = idx
            algo.wallet.now = idx
            algo.wallet.currentSlice = algo.currentSlice
            algo.OnData()
            algo.wallet.UpdateData(algo.currentSlice)


def ExportDataToCSV(tickers, startdate, enddate):
    for s in tickers:
        try:
            temppd = tda.get_price_history_day(s, startdate, enddate)
            temppd['datetime'] = temppd['datetime'] - (4 * 60 * 60 * 1000)
            temppd['datetime'] = pd.to_datetime(temppd['datetime'], unit='ms')
            temppd.set_index('datetime', inplace=True)
            temppd.to_csv(f"Resources/Data/{s}_daily_data.csv")
            logger.debug(s)
            logger.debug(temppd)
        except KeyError:
            logger.warning(colored(s, "red"))


def main(update, algo, start=datetime(month=3, day=2, year=2002), end=datetime.now()):
    algo = algo(start)

    if update:
        ExportDataToCSV(algo.Tickers + ["SPY"],
                        start, end)

    backtester = Backtester(start, end, algo.Tickers)
    backtester.PreProcess()
    try:
        backtester.RunBacktest(algo)
    except KeyboardInterrupt:
        algo.OnFinish(backtester.Market)
    else:
        algo.OnFinish(backtester.Market)
