import time, datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import dateutil

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
        return 'Ticker: %s \n Number of Shares: %s \n Current Value: %s \n Annualized Return: %s%%' % (self.ticker, self.num_shares, self.value, self.calculate_annual_return())

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
    
    def calculate_annual_return(self):
        """
        Calculates the average annualized return of the investment throughout its history.
        """

        start_date = datetime.datetime.strptime(self.history.iloc[0]['date'], '%m/%d/%y')
        end_date = datetime.datetime.strptime(self.history.iloc[-1]['date'], '%m/%d/%y')
        date_diff = dateutil.relativedelta.relativedelta(end_date, start_date)
        num_years = date_diff.years + date_diff.months/12 + (date_diff.days+1)/365.2425

        start_value = self.history.iloc[0]['value']
        end_value = self.history.iloc[-1]['value']
        total_return = (end_value - start_value)/(start_value)

        return (((1+total_return)**(1/num_years))-1)*100

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