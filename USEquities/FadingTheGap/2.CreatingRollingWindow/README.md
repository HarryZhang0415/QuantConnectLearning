# Creating a Rolling Window
## Creating A Rolling Window
A **RollingWindow** holds a set of the most recent entries of data. As we move from time t=0 forward, our rolling window will shuffle data further along to a different index until it leaves the window completely.

## Setting A Window Type and Length
When we create a rolling window we need to set the type of data it will use. See more about the data types available in QuantConnect such as float, TradeBar, and QuoteBar here.

The length of the window is specified in parentheses after the data type. Keep in mind the window is indexed from 0 up to Count-1.

    # Rolling window of 4 TradeBars (indexed from 0: 0, 1, 2, 3)
    self.window = RollingWindow[TradeBar](4) 

## Adding Entries To A Window
We update our rolling array with the **Add()** method, which adds a new element at the beginning of the window. The objects inserted must match the type of the **RollingWindow**.

    # Add the SPY trade bar to the window.
    self.window.Add(self.CurrentSlice["SPY"])

## Accessing Price Data
The latest data point is accessible with the algorithm **self.CurrentSlice** property. This is the same **Slice** object from **OnData**.

    def OnData(self):
        self.Debug("Called Event: " + str(self.CurrentSlice["SPY"].Price))