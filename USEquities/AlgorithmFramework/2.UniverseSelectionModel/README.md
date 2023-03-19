# Universe Selection Model

The Universe Selection Model systematically selects assets. It removes selection bias from the algorithm by filtering for assets to trade with programmed criteria.

![The San Juan Mountains are beautiful!](https://cdn.quantconnect.com/i/tu/UniverseModel5.jpg "San Juan Mountains")

Universe Models take in universe data, and return a list of symbol objects. QuantConnect provides dozens of premade universes for you to easily use in your algorithm.

## Manual Universes
The simplest universe, the Manual Universe Selection Model, accepts a hard coded list of symbols. You can create Symbol objects with the Symbol.Create function.

    def Initialize(self):
        # Set a Manual Universe Selection Model initialized with the symbols list 
        self.symbols = [Symbol.Create("SPY", SecurityType.Equity, Market.USA)]
        self.AddUniverseSelection(ManualUniverseSelectionModel(self.symbols))

## Universe Settings
The resolution of the assets added to the universe is configured by the self.UniverseSettings.Resolution property.

    # Set to daily resolution 
    self.UniverseSettings.Resolution = Resolution.Daily