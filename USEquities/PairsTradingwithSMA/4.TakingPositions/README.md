# Taking Positions
## Timing of Insight Emission

We can emit an insight group for our pair of assets with a conditional statement that triggers an event when the spread is greater than the threshold.

When the current spread is greater than the upper threshold, it means the difference in asset prices is widening and will likely revert back to the mean. When this happens we go long one asset, and short the other.

In this case in **Update()** we take a long position on the first asset in the pair with **InsightDirection.Up** and we sell the second asset in the pair with **InsightDirection.Down**.

    if spread > upperthreshold:
        return Insight.Group(
            [
                Insight.Price(self.pair[0].Symbol, self.period, InsightDirection.Up),
                Insight.Price(self.pair[1].Symbol, self.period, InsightDirection.Down)
            ])
    
Conversely, when the current spread is lower than the lower threshold, it means the difference in asset prices is abnormally low, and the price will likely soon widen.

In this case we take a short position on the first asset in the pair with **InsightDirection.Down** and we purchase the second asset in the pair with an **InsightDirection.Up**.

    if spread < lowerthreshold:
        return Insight.Group(
            [
                Insight.Price(self.pair[0].Symbol, self.period, InsightDirection.Down),
                Insight.Price(self.pair[1].Symbol, self.period, InsightDirection.Up)
            ])
        
An insight is a prediction of the asset movements for a period of time. This is set with the period arguement of type TimeSpan.

    self.period = timedelta(hours=2)

## Taking Positions
The insights emitted from the Alpha Model are sent to our Portfolio Construction Model to determine our positions. We are taking a hedged position by offsetting risk from investing in one asset by taking a long position and selling a short position. This long-short balanced trade is automatically calculated by the **EqualWeightingPortfolioConstructionModel**.

## Logging Positions
We can observe our positions taken at the close of each day by creating a new event handler **OnEndOfDay()**. This method lives in your algorithm class.

    class SMAPairsTrading(QCAlgorithm):
        def OnEndOfDay(self, symbol):
            self.Log("Taking a position of " + str(self.Portfolio[symbol].Quantity) + " units of symbol " + str(symbol))
    
