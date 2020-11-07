# Stock Comparison Tool

This Stock Comparison Tool will compare the returns of any stock/etf contained in the TD Ameritrade database.

## Usage

Given any number of stock/etfs, an investment period, and an initial investment amount (in dollars), the Stock Comparison Tool will graph and analyze the return of each stock/etf over the investment period. This helps users visualize how profitable investing in the stock market, or a specific asset, would have been in the past.

Note: The Stock Comparison Tool does not yet account for dividends.

## Getting Started

### Prerequisites

1. Get a free TD Ameritrade API Key from the [TD Ameritrade Developer Site](https://developer.tdameritrade.com/content/getting-started#createAccount)
2. Enter your API Key in config.py under CONSUMER_KEY

### Installation

1. Download and install the pandas, matplotlib, and requests modules using pip
```
pip install pandas
```

## Authors

* **David Li** - [GitHub](https://github.com/lidav953) - [LinkedIn]
(https://www.linkedin.com/in/davidli1996/)
## Motivation

I wanted a straightforward way to compare the historical performance of specific stocks in my personal trading account without having to look each one up individually and manually calculate their returns. Also, this program is an easy way to teach people about the benefits and pitfalls of investing their money in the stock market.