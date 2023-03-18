# Tracking Security Changes
## Monitoring Universe Changes
When the universe constituents change (securities are added or removed from the algorithm) the algorithm generates an **OnSecuritiesChanged** event which is passed information about the asset changes.

    def OnSecuritiesChanged(self, changes):
        pass

## Universe Selection Timing
You can monitor and act on these events in the **OnSecuritiesChanged()** event handler. The universe selection is performed at midnight each day, to choose the assets for the next trading day. These assets are added in minute resolution by default.

## Using Log()
Algorithms can write log files for later analysis using **self.Log(string message)**. At the end of the backtest a link will be presented in your console to view your results.

    self.Log(f"OnSecuritiesChanged({self.Time}):: {changes}")