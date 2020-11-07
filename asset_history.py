import requests
import time, datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from config import CONSUMER_KEY

class Asset:
    """
    Contains the price data of an asset between two specific dates.
    """

    def __init__(self, ticker, start_date, end_date):
        """
        Initializes an asset.
        ticker = the trading ticker of the asset
        start_date = the first date of data, formatted as 'month/day/year'
        end_date = the last date of data, formatted as 'month/day/year'
        price_data = the price history of the asset from start_date to end_date
        """
        self.ticker = ticker
        self.start_date = time.mktime(time.strptime(start_date, "%m/%d/%Y"))
        self.end_date = time.mktime(time.strptime(end_date, "%m/%d/%Y"))
        self.price_data = read_price_data(self.ticker, self.start_date, self.end_date)

    def get_ticker(self):
        """
        Returns the ticker of the asset.
        """
        return self.ticker

    def get_price_data(self):
        """
        Returns the daily price data of this asset as a pandas DataFrame
        """
        return self.price_data

def read_price_data(ticker, start_date, end_date):
    """
    Reads the daily price data of this asset within the given date range.
    """

    # Daily prices endpoint
    endpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format(ticker)

    # Define the payload
    payload = {'apikey' : CONSUMER_KEY,
            'periodType' : 'year',
            'frequencyType' : 'daily',
            'frequency' : '1',
            'endDate' : str(int(end_date)*1000),
            'startDate' : str(int(start_date)*1000),
            'needExtendedHoursData' : 'true'}

    # Make a request and convert it to a dictionary
    content = requests.get(url=endpoint, params=payload)
    data = content.json()
    #print(data)

    # Convert data to a pandas dataframe
    open = []
    close = []
    dates = []
    for candle in data['candles']:
        open.append(candle['open'])
        close.append(candle['close'])

        date = datetime.datetime.fromtimestamp(int(candle['datetime'])/1000).strftime("%x")
        dates.append(date)

    price_data = pd.DataFrame({'date' : dates,
                            'open' : open,
                            'close' : close,})
    return price_data

    """
    open = []
    high = []
    low = []
    close = []
    volume = []
    dates = []
    for candle in data['candles']:
        open.append(candle['open'])
        high.append(candle['high'])
        low.append(candle['low'])
        close.append(candle['close'])
        volume.append(candle['volume'])

        date = datetime.datetime.fromtimestamp(int(candle['datetime'])/1000).strftime("%x")
        dates.append(date)

    price_data = pd.DataFrame({'Date' : dates,
                            'Open' : open,
                            'High' : high,
                            'Low' : low,
                            'Close' : close,
                            'Volume' : volume})
    return price_data
    """
    
def plot_close_prices(asset):
    """
    Plots the daily close prices of an asset
    """
    price_data = asset.get_price_data()
    price_data.plot(x = 'Date', y = 'Close')
    frequency = 10 # every 10 trading days (or approx. 2 weeks)
    my_xticks = asset.price_data['Date'].tolist()[::frequency]
    plt.xticks(ticks = price_data.index[::frequency], labels = my_xticks, rotation = 45)
    plt.show()