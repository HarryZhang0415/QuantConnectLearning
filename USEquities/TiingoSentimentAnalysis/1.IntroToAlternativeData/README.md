# Introducing Alternative Data
## Importing Alternative Data
QuantConnect provides a growing number of alternative data sets you can import into your algorithm. This data covers corporate fundamentals, macro economics, news and events, price data, and sentiment data.

## Setting Up A Manual Universe

The simplest universe, the Manual Universe Selection Model, accepts a hard coded list of symbols. We add an instance of our **ManualUniverseSelectionModel()** in our **Initialize()** method. It is initialized with a list of symbols.

    self.SetUniverseSelection(ManualUniverseSelectionModel(symbols))

You can create Symbol objects with the **Symbol.Create** function, which accepts ticker, **SecurityType** and **Market** parameters.

    symbols = [Symbol.Create("SPY", SecurityType.Equity, Market.USA)]

