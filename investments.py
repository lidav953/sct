import time, datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

class Investment:
    """
    Contains an investment in an asset.
    """

    def __init__(self, ticker, initial_investment, initial_price, start_date):
        """
        Initializes an investment.
        ticker = the trading ticker of the asset
        value = the monetary value of the investment
        num_shares = the number of shares owned
        history = pandas dataframe containing the history of this investment
        """
        self.ticker = ticker
        self.value = initial_investment
        self.num_shares = initial_investment/initial_price
        self.history = pd.DataFrame(columns = ['date', 'value'])
        self.update_history(start_date)

    def __str__(self):
        return 'Ticker: %s \n Number of Shares: %s \n Current Value: %s' % (self.ticker, self.num_shares, self.value)

    def update_value(self, price, date):
        """
        Updates the value of the investment with the new asset price.
        """
        self.value = self.num_shares*price
        self.update_history(date)
    
    def update_history(self, date):
        """
        Updates investment history.
        """
        self.history = self.history.append({'date':date, 'value':self.value}, ignore_index = True)

    def get_shares(self):
        """
        Returns the number of shares owned.
        """
        return self.num_shares

    def get_value(self):
        """
        Returns the current value of the investment.
        """
        return self.value

    def get_history(self):
        """
        Returns the investment history.
        """
        return self.history
    
    def get_ticker(self):
        """
        Returns the ticker of this investment.
        """
        return self.ticker