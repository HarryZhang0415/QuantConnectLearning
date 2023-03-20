# What is Pairs Trading?
## Introducing Pairs Trading
Often when two assets share related customer bases, or sell similar products, their asset price can move together. For this lesson we are reviewing Coca-Cola and Pepsi, two soft-drink companies both influenced by health sentiment, the seasons, and price of sugar.
![Coca vs Pepsi](https://cdn.quantconnect.com/i/tu/price_series_stock_pairs1.png)
Pairs trading is a market neutral strategy, meaning the strategy returns are uncorrelated with market returns. A pairs trade is triggered when the difference between a pair of assets crosses an upper or lower threshold. The strategy's goal is to sell whichever is the expensive stock of the pair at the time and buy the cheaper stock.

## Selecting Pairs
In general, assets are considered a pair when the difference between the two assets mean revert, or are cointegrated. Cointegration is a statistical property of a time series. We expect the price difference between the pair to come back to a common long-run mean.

Another criteria for the pair is stationarity. This means the mean and variance of the series do not vary over time. Each asset price-time series could be non-stationary but the price difference between the pair should be stationary. See [more on stationary time series](https://github.com/PythonCharmers/QuantFinance/blob/master/notebooks/Module%201.6.2%20-%20Stationarity.ipynb) and [testing for stationarity](https://www.quantconnect.com/forum/discussion/6859/from-research-to-production-stationary-processes-and-z-scores/p1).

## Algorithm Design
We control our selection of pairs and our calculation of the optimal trigger ("threshold") for trades. Using the QC algorithm framework, we select our asset pairs in the Universe model and create our pairs trading signals in the Alpha model.