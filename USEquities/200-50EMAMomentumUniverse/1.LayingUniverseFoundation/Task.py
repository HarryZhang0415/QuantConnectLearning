'''
Task Objectives
Filter out the stocks less than $10.
Reverse sort coarse by dollar volume to get the 10 highest volume stocks.
Save the result to self.selected.
Liquidate securities leaving the universe in the OnSecuritiesChanged event.
Allocate 10% holdings to each asset added to the universe.
'''

from AlgorithmImports import *
class EMAMomentumUniverse(QCAlgorithm):
    
    def Initialize(self):
        self.SetStartDate(2019, 1, 7)
        self.SetEndDate(2019, 4, 1)
        self.SetCash(100000)
        self.UniverseSettings.Resolution = Resolution.Daily
        self.AddUniverse(self.CoarseSelectionFunction)
        self.selected = None
    
    def CoarseSelectionFunction(self, coarse):
        #1. Sort coarse by dollar volume
        #2. Filter out the stocks less than $10 and return selected
        sortedByDollarVolume = sorted(coarse, key=lambda c: c.DollarVolume, reverse=True)
        self.selected = [c.Symbol for c in sortedByDollarVolume if c.Price > 5][:10]
        return self.selected
        
    def OnSecuritiesChanged(self, changes): 
        #3. Liquidate securities leaving the universe
        #4. Allocate 10% holdings to each asset added to the universe
        for security in changes.RemovedSecurities:
            self.Liquidate(security.Symbol)
        
        for security in changes.AddedSecurities:
            self.SetHoldings(security.Symbol, 0.10)
        
        return
        
