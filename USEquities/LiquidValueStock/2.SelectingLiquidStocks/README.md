# Selecting Liquid Stocks
## Our Two-Stage Filter
To filter for securities based on fundamental data, we use a two-stage filter. We've used the first stage of the filter, the Coarse Universe Selection function, in previous lessons. The results of the coarse selection filter are passed into the second filter, the Fine Universe Selection function. It filters based on fundamental data and returns symbol objects.

![Two-Stage Filter](https://cdn.quantconnect.com/docs/i/filters.png)

## Managing Data Frequency
We control how frequently we update our universe with our algorithm's **Time** property. The **Time** property has year, month, and day objects. We can access an index value of the object with an integer value (eg. **self.lastMonth** = -1). When it's not time to bring in new data, we return **Universe.Unchanged**.

    def SelectCoarse(self, algorithm, coarse):       
    # Return Universe.Unchanged for the time when we don't bring in new data 
        if self.lastMonth == algorithm.Time.month:
            return Universe.Unchanged
        self.lastMonth = algorithm.Time.month
    
## Selecting Liquid Stocks
Only 5,000 assets have fundamental data. To use the fine filter, the coarse filter needs to pass in symbols that have fundamental data. When working with fundamental data you should always include the "HasFundamentalData" filter in your Coarse Universe filter.

    def SelectCoarse(self, algorithm, coarse): 
        # Sort symbols by Dollar Volume and if fundamental data exists, descending
        sortedByDollarVolume = sorted([x for x in coarse if x.HasFundamentalData],
                key=lambda x: x.DollarVolume, reverse=True)
        return [x.Symbol for x in sortedByDollarVolume[:100]]

