'''
Task Objectives
We want to trade the 8 most liquid symbols, worth more than $10 per share. To get this list of symbols we will need to sort our list of coarse objects ("coarse") by dollar volume. Then we want to use a list comprehension filter to exclude penny stocks, and get the symbol objects.

Sort your symbols descending by dollar volume and save to sortedByDollarVolume
Set self.filteredByPrice to symbols with a price of more than $10 per share
Return the 8 most liquid symbols from the self.filteredByPrice list
'''

class LiquidUniverseSelection(QCAlgorithm):
    
    filteredByPrice = None

    def Initialize(self):
        self.SetStartDate(2019, 1, 11)  
        self.SetEndDate(2019, 7, 1) 
        self.SetCash(100000)  
        self.AddUniverse(self.CoarseSelectionFilter)
        
    def CoarseSelectionFilter(self, coarse):
        
        #1. Sort descending by daily dollar volume
        sortedByDollarVolumn = sorted(coarse, key=lambda c: c.DollarVolume, reverse=True)
        
        #2. Select only Symbols with a price of more than $10 per share
        symbols_by_price = [c.Symbol for c in sortedByDollarVolumn if c.Price > 5]
        
        #3. Return the 8 most liquid Symbols from the filteredByPrice list
        self.filteredByPrice = symbols_by_price[:8]
        return self.filteredByPrice
    
