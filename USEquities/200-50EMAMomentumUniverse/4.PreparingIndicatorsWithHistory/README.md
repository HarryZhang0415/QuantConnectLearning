# Preparing Indicators with History
## Applying a History Function
We need to prepare our indicators with data. With the QuantConnect History API, we request data for symbols as a pandas dataframe.

The History API has many different helpers, the simplest of these gets data for a single symbol.

    history = self.History(symbol, 200, Resolution.Daily)

## Using History DataFrame

Each row of the history result represents the prices at a point of time. Each column of the DataFrame is a property of the price data (e.g. open, high, low, close).

History data is returned in ascending order from oldest to newest. If no resolution is chosen the default is Resolution.Minute. We can iterate over the results of a history call using **itertuples()**. The history DataFrame has two indexes; Symbol(0) and Time(1). You can access the time of a row by using **row.Index[1]**. The column names of the history result are lowercase.

    for bar in history.itertuples():
        self.fast.Update(bar.Index[1], bar.close)
        self.slow.Update(bar.Index[1], bar.close)