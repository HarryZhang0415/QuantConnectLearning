# Tracking Security Changes
## Security Changes Review
By default, QuantConnect's universe selection model selects assets daily at midnight. When the universe constituents change, the algorithm generates an **OnSecuritiesChanged** event, which receives information about the asset changes.

We can efficiently update these asset changes using the **OnSecuritiesChanged()** event handler. The data includes **AddedSecurities** and **RemovedSecurities** properties, which return a list of security objects.

    # Access securities being added and removed from the OnSecuritiesChanged method 
    def OnSecuritiesChanged(self, algorithm, changes):
        for security in changes.AddedSecurities:
            pass
        for security in changes.RemovedSecurities:
            pass

## Security Fundamentals Property
Outside of the Universe Selection Model, fundamental data for securities is accessed using the **Fundamentals** property on the security object.

    # Examples of accessing Fundamentals properties
    for security in changes.AddedSecurities:
        security.Fundamentals.AssetClassification
        security.Fundamentals.ValuationRatios
        security.Fundamentals.CompanyReference 
    


## Maintaining Dictionary of Data
One way to store fundamental data is in a container such as a data class or dictionary indexed by the security symbol. To make our algorithms efficient, when an asset is added or removed to our universe, add or remove the security symbol and its fundamental data from the data storage.