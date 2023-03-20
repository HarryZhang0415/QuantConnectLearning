# Monitoring for Price Deviance
## Smoothing Price Deviance
The absolute difference in price is too noisey to use as a trading signal. Because of this we will use a Simple Moving Average indicator to calculate mean price difference over a period of time

    def __init__(self):
        self.spreadMean = SimpleMovingAverage(500)

## Updating Spread ("Synthetic Asset")
We update our spread with the latest data in the **Update()** method by using the arguments **algorithm.Time** and **spread**.

    spread = self.pair[1].Price - self.pair[0].Price
    # Update the spread of means over time 
    self.spreadMean.Update(algorithm.Time, spread)
    # Update the spread of standard deviations over time
    self.spreadStd.Update(algorithm.Time, spread)

## Defining Trading Thresholds
Trading thresholds are often defined by the standard deviations from an average. For pairs trading this is the standard deviations of the current spread, from its average. The upper and lower bounds of these thresholds are set as some standard deviations away from our average price spread.

![Spread](https://cdn.quantconnect.com/i/tu/spread_and_threshold_example2.png)

When the spread crosses the upper or lower threshold, a pair of insights are emitted. We can set the upper and lower threshold in our **Update()** method using our indicator's **Current.Value** property.

    def __init__(self):
        self.spreadStd = StandardDeviation(500)
    def Update(self, algorithm, data):
        upperthreshold = self.spreadMean.Current.Value + self.spreadStd.Current.Value
        lowerthreshold = self.spreadMean.Current.Value - self.spreadStd.Current.Value
        