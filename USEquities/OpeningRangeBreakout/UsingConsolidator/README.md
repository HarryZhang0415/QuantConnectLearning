# Using the Output of the Consolidator
## Using Our Consolidated Data

As we have requested equities data, the consolidated bar's type is **TradeBar**. It has the properties Open, High, Low, Close and Volume for a given period of time.

    def OnDataConsolidated(self, bar):
        # bar.Time
        # bar.Open
        # bar.High
        # bar.Low
        # bar.Close 
    
## Opening Short Positions
Short positions are when you are betting the market will fall in value. When you place a "short trade" you are borrowing someone else's stocks for a while to sell them. When you "close" a short position you are buying back the stocks you borrowed at the new market price.

## Going Short In QuantConnect
In QuantConnect, we don't need to place a separate order type to enter a short position. We can use a scale of 1 to -1 in **self.SetHoldings** to place a long or short order. Going long is denoted by ordering a positive number, and short a negative one. QC does not support hedging (long and short at the same time).

    # Go 100% short on SPY
    if data["SPY"].Close < self.openingBar.Low:
        self.SetHoldings("SPY", -1)