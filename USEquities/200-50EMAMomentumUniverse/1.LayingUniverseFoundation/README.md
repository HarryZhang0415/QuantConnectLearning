# Laying Our Universe Foundation
In this lesson we will using two indicators to perform selection on a universe of securities.

## Creating Our Universe
Recall that we use coarse universe selection to create a set of stocks based on dollar-volume, and price. To create our universe of assets we need to pass a coarse selection filter function to the **self.AddUniverse()** method in our initializer.

    # Pass the filter function into AddUniverse in your Initializer
    def Initialize(self):
        self.AddUniverse(self.CoarseSelectionFilter)
    # Create a filter function    
    def CoarseSelectionFilter(self, coarse):
        pass 

## Using Our Filter
Our CoarseSelectionFilter must return a list of symbols, which LEAN automatically subscribes to and adds to our algorithm.

To filter and sort our stocks we can use lambda functions and list comprehension.

    # Use the sorted method and lambda to get keys in ascending order (greatest to least in DollarVolume)
    sortedByDollarVolume = sorted(coarse, key=lambda c: c.DollarVolume, reverse=True)

    # Use list comprehension to get symbols from your sorted list 
    # with a price more than $5 per share and get the top 10 symbols
    [c.Symbol for c in sortedByDollarVolume if c.Price > 5][:10]

## Adding and Removing Securities

The **OnSecuritiesChanged** event fires whenever we have changes to our universe. It receives a **SecurityChanges** object containing references to the added and removed securities. The **AddedSecurities** and **RemovedSecurities** properties are lists of security objects.

 
    # Liquidate the securities that are no longer in our universe
    for security in changes.RemovedSecurities:
        self.Liquidate(security.Symbol)
    # Set Holdings for the securities added to our universe 
    for security in changes.AddedSecurities:
        self.SetHoldings(security.Symbol, 0.10)