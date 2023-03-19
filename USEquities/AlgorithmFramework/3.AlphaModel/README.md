# Alpha Model

The Alpha Model generates predictions of the exected returns for assets in our universe.

## Data Flow: Alpha Model
![Data Flow: Alpha Model](https://cdn.quantconnect.com/i/tu/AlphaModel4.jpg "Data Flow: Alpha Model")

Our Alpha Model consumes price data provided by the Universe Selection Model, and the results are emitted as trade signals called Insights. An Insight indicates the direction, magnitude, confidence, weight and period of our prediction.

## Setting An Alpha Model
We set our Alpha Model in Initialize().

    def Initialize(self):
        # Set the alpha model to an instance of MOMAlphaModel()
        self.SetAlpha(MOMAlphaModel())

## Alpha Model Class Structure
Alpha models must inherit from the AlphaModel base class. They should implement two functions; **OnSecuritiesChanged()** and **Update()**.

    class MOMAlphaModel(AlphaModel):
        def __init__(self):
            pass 
        def OnSecuritiesChanged(self, algorithm, changes):
            pass
        def Update(self, algorithm, data):
            pass

## Initializing Alpha State
When assets are added or removed from our universe they will trigger an **OnSecuritiesChanged()** event. We should use this event to setup any state required for our alpha calculations. The method provides the algorithm object, and a list of securities changes. For example, we could generate indicators for each symbol in this method and save the symbols and indicators to a dictionary.

    def __init__(self):
        self.mom = []

    def OnSecuritiesChanged(self, algorithm, changes):
    # e.g. Initialize a 14-day momentum indicator for each symbol 
        for security in changes.AddedSecurities:
            symbol = security.Symbol
            self.mom.append({"symbol":symbol, "indicator":algorithm.MOM(symbol, 14, Resolution.Daily)})
    
## Emitting Insights
The **Update()** method is called each time the algorithm receives data for subscribed securities. After analysis, the Alpha Model should emit insights for assets it would like to trade.

    def Update(self, algorithm, data):
        # Perform analysis, then and emit insights:
        return Insight.Price("SPY", timedelta(1), InsightDirection.Up)

## Emitting Grouped Insights
We can return a set of Insights together as a group, which signal to the execution model that the insights need to be traded simultaneously.

    def Update(self, algorithm, data):
        return Insight.Group([
                # Create a grouped insight
                Insight.Price("IBM", timedelta(1), InsightDirection.Up), 
                Insight.Price("AAPL", timedelta(1), InsightDirection.Flat)
            ])