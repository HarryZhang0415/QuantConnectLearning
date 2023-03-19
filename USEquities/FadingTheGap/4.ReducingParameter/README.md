# Reducing a Parameter
## Reducing Parameters Using Standard Deviation
Modern quant research suggests we should use as few parameters as possible. In this task we'll replace the arbitary -$10 move with a measurement of the standard deviation to replace a parameter with a statistical "confidence".

Assuming asset prices follow a normal distribution, we can use standard deviation to measure an asset's volatility. In a normal distribution, 68% of values are within 1 standard deviation of the mean, 95% of values are within 2 standard deviations of the mean, and 99% of values are within 3 standard deviations of the mean.

## Creating an Indicator Manually
QuantConnect provides the ability to add indicators manually. When we create an indicator manually, we control what data goes into it. Each manual indicator is slightly different, but the standard deviation takes a name and period. More on this topic can be found in the documentation here.

    # Create an indicator StandardDeviation 
    # for the symbol TSLA with a 30 "value" period 
    self.volatilty = StandardDeviation("TSLA", 30)
    self.rsi = RelativeStrengthIndex("MyRSI", 200)
    self.ema = ExponentialMovingAverage("SlowEMA", 200)

## Updating Our Indicator
When we create a manual indicator object, we need to update it in order to create valid indicator values. All manual indicators have an Update method which takes a time and a value.

    # Update the state of our indicator with TSLA's close price
    def OnData(self, data):
        if data["SPY"] is not None: 
            self.volatility.Update(self.Time, data["SPY"].Close)

When you're using the helper methods the updates are done automatically (e.g. RSI(), EMA()). When using a combination of OnData and Scheduled Events keep in mind that **scheduled** events trigger before our **OnData** events, so your indicator might not be updated yet.

## Accessing Indicator Values

Manually created indicators values are accessed just like their automatic counterparts.

    # Accessing current value of standard deviation
    x = self.volatility.Current.Value