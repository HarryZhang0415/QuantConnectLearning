# Warming Our Pair Spread
## Preparing Our Indicators
Finally, we're going to prepare our spread deviation indicators by using a history call to ensure the algorithm can begin trading immediately. As we saw in a previous lesson, we can get historical price data for each symbol in the pair with the History API, which requests data for symbols.

For example, in **OnSecuritiesChanged()** we can use list comprehension to iterate through each symbol in the pair and update it with 500-bars of previous data. History data for the pair is stored in a dataframe.

    def OnSecuritiesChanged(self, algorithm, changes):
        history = algorithm.History([x.Symbol for x in self.pair], 500)

Using unstack we can reduce the history result pandas dataframe to just the close column.

    def OnSecuritiesChanged(self, algorithm, changes):
        history = history.close.unstack(level=0)

## Iterating Through History Data
Each row of the history dataframe is a tuple where tuple[0] is the time, tuple[1] is the close price for the first asset, and tuple[2] is the close price for the second asset. We can iterate through each row and update our spread indicators with the price difference between asset A and B close prices.

    def OnSecuritiesChanged(self, algorithm, changes):
        for tuple in history.itertuples():
            self.spreadMean.Update(tuple[0], tuple[2]-tuple[1])
            self.spreadStd.Update(tuple[0], tuple[2]-tuple[1])