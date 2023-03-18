'''
Task Objectives
For this strategy, we want to always have 10% of our cash allocated to each of the securities in the universe. When a security leaves the universe liquidate any holdings we have in that asset. Once all the securities are liquidated, purchase the new universe securities.

In the OnSecuritiesChanged event, loop over the removed securities, liquidating each one.
In the OnSecuritiesChanged event, loop over the added securities, using SetHoldings to allocate 10% to each.
Note: We changed the data resolution to daily. In next task will discuss configuring more universe settings.
'''

class LiquidUniverseSelection(QCAlgorithm):
    
    filteredByPrice = None
    
    def Initialize(self):
        self.SetStartDate(2019, 1, 11)  
        self.SetEndDate(2019, 7, 1) 
        self.SetCash(100000)  
        self.AddUniverse(self.CoarseSelectionFilter)
        # Ignore this for now, we'll cover it in the next task.
        self.UniverseSettings.Resolution = Resolution.Daily 

    def CoarseSelectionFilter(self, coarse):
        sortedByDollarVolume = sorted(coarse, key=lambda x: x.DollarVolume, reverse=True) 
        filteredByPrice = [x.Symbol for x in sortedByDollarVolume if x.Price > 10]
        return filteredByPrice[:8]
   
    def OnSecuritiesChanged(self, changes):
        self.changes = changes
        self.Log(f"OnSecuritiesChanged({self.UtcTime}):: {changes}")
        
        #1. Liquidate removed securities
        for security in changes.RemovedSecurities:
            if security.Invested:
                self.Liquidate(security.Symbol)
        
        #2. We want 10% allocation in each security in our universe
        for security in changes.AddedSecurities:
            self.SetHoldings(security.Symbol, 0.1)
