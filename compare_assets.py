"""
The primary program that collects user input and shows stock performance.
"""

from asset_history import *
from investments import *
import matplotlib.pyplot as plt
import matplotlib
import time, datetime

def get_tickers():
    """
    Gets the tickers for the assets to be compared from the user.
    """
    num_tickers = get_num_tickers()
    tickers = []
    for x in range(num_tickers):
        ticker = input('Enter a stock/etf ticker (ie SPY): ')
        tickers.append(ticker.upper())
    return tickers

def get_num_tickers():
    """
    Gets the number of tickers to be compared from the user.
    """
    while True:
        try:
            num_tickers = int(input('Enter the number of stocks/etfs to compare: '))
        except ValueError:
            print('Please enter an integer.\n')
        else:
            return num_tickers

def get_date(msg):
    """
    Gets a date from the user.
    """
    while True:
        try:
            date = input(msg)
            error_date = time.mktime(time.strptime(date, "%m/%d/%Y"))
        except:
            print('Please enter the date in the proper format.\n')
        else:
            return date

def get_initial_investment():
    """
    Gets the initial investment in each asset from the user.
    """
    while True:
        try:
            initial_investment = float(input('Enter the starting investment for each stock/etf. '))
        except ValueError:
            print('Please enter a valid amount of money.\n')
        else:
            return initial_investment

def initialize_assets(tickers, start_date, end_date):
    # Initialize the list of assets.
    assets = []
    for ticker in tickers:
        assets.append(Asset(ticker, start_date, end_date))
    return assets

def invest(assets, initial_investment, start_date):
    """
    Initializes each investment with $initial_investment.
    Tracks the growth of each investment over the investment period
    """

    """
    For each asset, graph the cumulative return of $100,000 over the given time frame.
    1. On start_date, buy shares with $100,000 (can be fractional)
    2. Calculate new value of portfolio each day.
    Challenge: Dividends are paid & reinvested on payment date.
    Challenge: Calculate annual & total returns
    ^ can the above all be written directly into the Asset class?
    """

    investments = []

    for asset in assets:
        price_data = asset.get_price_data()
        ticker = asset.get_ticker()
        initial_price = price_data.iloc[0]['open']
        inv = Investment(ticker, initial_investment, initial_price, datetime.datetime.strptime(start_date, '%m/%d/%Y').strftime("%x"))

        for index, row in asset.get_price_data().iterrows():
            inv.update_value(row['close'], row['date'])

        investments.append(inv)

    return investments

def graph_history(investments, tickers):
    """
    Graphs all investment performance.
    """
    for inv in investments:
        history = inv.get_history()
        plt.plot(history['date'], history['value'])
        frequency =  10 #one data point per 10 trading days
        my_xticks = history['date'].tolist()[::frequency]
        plt.xticks(ticks=history.index[::frequency], labels=my_xticks, rotation=45)

    plt.legend(tickers)
    plt.show()

def print_result(investments, tickers):
    """
    Prints the final result of each investment over the time period.
    """

    for inv in investments:
        print(inv)

if __name__ == "__main__":
    #tickers = ['SPY', 'QQQ', 'IWM']
    #start_date = '01/01/2020'
    #end_date = '09/01/2020'
    #initial_investment = 100000

    print("This is the Stock Comparison Tool, where you can invest money in stocks/etfs and compare their historical returns over any dates you choose.")
    
    tickers = get_tickers()
    start_date = get_date('Enter the starting investment date in the format mm/dd/yyyy: ' )
    end_date = get_date('Enter the ending investment date in the format mm/dd/yyyy: ')
    initial_investment = get_initial_investment()

    assets = initialize_assets(tickers, start_date, end_date)
    investments = invest(assets, initial_investment, start_date)
    graph_history(investments, tickers)
    print_result(investments, tickers)