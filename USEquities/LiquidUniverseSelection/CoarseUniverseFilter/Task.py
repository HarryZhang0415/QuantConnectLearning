'''
Task Objectives
Set up the foundation for performing universe selection.

Create a filter function CoarseSelectionFilter(self, coarse).
In your filter function, save coarse to self.coarse, then return Universe.Unchanged.
Pass the name of filter function into self.AddUniverse to use coarse fundamental data.
'''

class LiquidUniverseSelection(QCAlgorithm):
    
    filteredByPrice = None
    coarse = None
    
    def Initialize(self):
        self.SetStartDate(2019, 1, 11)  
        self.SetEndDate(2019, 7, 1) 
        self.SetCash(100000)  
        
        #3. Add a Universe model using Coarse Fundamental Data and set the filter function 
        self.AddUniverse(self.CoarseSelectionFilter)
        
    #1. Add an empty filter function
    def CoarseSelectionFilter(self, coarse):
        #2. Save coarse as self.coarse and return an Unchanged Universe
        self.coarse = coarse
        return Universe.Unchanged
