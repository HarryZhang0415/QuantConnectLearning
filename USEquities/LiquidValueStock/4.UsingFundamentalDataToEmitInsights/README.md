# Using Fundamental Data to Emit Insights
## Accessing Fundamental Data in the Alpha Model
While we pick the securities with universe selection, we decide which we will long and short in the Alpha Model. Fundamental data selected through the Universe Model is not passed into the Alpha Model, but we may need to access fundamental data again in our Alpha Model. We can do this with the **security.Fundamentals** property.

    class LongShortEYAlphaModel(AlphaModel):    
    def Update(self, algorithm, data):
        # For loop to emit insights with insight directions 
        # based on whether earnings yield is greater or less than zero once a month
        for security in algorithm.ActiveSecurities.Values:
            direction = 1 if security.Fundamentals.ValuationRatios.EarningYield > 0 else -1 
            insights.append(Insight.Price(security.Symbol, timedelta(28), direction)) 
        return insights

## Managing Insight Frequency
We want to emit insights only when we have changes in our universe symbols we also use algorithm **Time**. We do this in our **Update()** method of our Alpha Model class.

    if self.lastMonth == algorithm.Time.month:
        return insights
    self.lastMonth = algorithm.Time.month

## Building a Market Neutral Alpha
A [market-neutral](https://www.investopedia.com/terms/m/marketneutral.asp) Alpha attempts to take an equal weighting of long and short positions.

The actual execution of the alpha signals is handled by the Equal Weighting Portfolio Construction Model. Behind the scenes this model allocates a fixed fraction of our buying power to both Up and Down insight targets.