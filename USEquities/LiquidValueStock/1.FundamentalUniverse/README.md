# Requesting a Fundamental Universe
## Long-Short Strategies
A long-short strategy purchases securities that are expected to increase in value and shorts securities that are expected to decrease in value to balance out the bias of the portfolio. This balance of long and short is called "portfolio neutrality", and aims to make our strategy robust through a variety of market conditions.

## Liquid Value Stocks
We can easily buy and sell a security when a large volume of its shares are traded daily. A stock is liquid when it can be easily traded without significantly affecting the stock's price.

Value stocks are a category of stocks that seem to be trading for less than their intrinsic value. Value can be measured with fundamental data, which is information other than price itself, like PE Ratios, and Earnings.

## Using Fundamental Data
QuantConnect offers Morningstar fundamental data for approximately 5,000 stocks since 1998. We can use this fundamental data to select our universe of assets for trading.

## Requesting a Fundamental Universe
To create a fundamental universe we extend from the **FundamentalUniverseSelectionModel** base class. When extending from this class we must define the **SelectCoarse()** and **SelectFine()** methods. We'll call our universe a **LiquidValueUniverseSelectionModel**.

    class LiquidValueStocks(QCAlgorithm):
        def Initialize(self):
            self.AddUniverseSelection(LiquidValueUniverseSelectionModel())

    class LiquidValueUniverseSelectionModel(FundamentalUniverseSelectionModel):
        def __init__(self):
            # Access functionality of pre-built classes with the super() function
            super().__init__(True, None)
        def SelectCoarse(self, algorithm, coarse):
            return Universe.Unchanged
        def SelectFine(self, algorithm, fine):
            return Universe.Unchanged