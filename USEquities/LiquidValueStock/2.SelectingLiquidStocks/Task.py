'''
Task Objectives
In our algorithm we will update our universe of symbols once a month. Let's define our Universe Model's constructor and coarse selection method.

In the coarse selection method, use the algorithm Time property and month object to update our universe of symbols once a month. For all other days, return Universe.Unchanged.
Update the self.lastMonth variable with the current month.
Sort symbols by dollar volume in descending order if they have fundamental data.
Return the top 100 symbols by dollar volume.
'''

from AlgorithmImports import *
from Selection.FundamentalUniverseSelectionModel import FundamentalUniverseSelectionModel
class LiquidValueStocks(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2016, 10, 1)
        self.SetEndDate(2017, 10, 1)
        self.SetCash(100000)
        self.UniverseSettings.Resolution = Resolution.Hour
        self.AddUniverseSelection(LiquidValueUniverseSelectionModel())
        self.AddAlpha(NullAlphaModel())
        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel())
        self.SetExecution(ImmediateExecutionModel())

class LiquidValueUniverseSelectionModel(FundamentalUniverseSelectionModel):
    
    def __init__(self):
        super().__init__(True, None)
        self.lastMonth = -1 
    
    def SelectCoarse(self, algorithm, coarse):
        
        #1. If it isn't time to update data, return the previous symbols 
        if self.lastMonth == algorithm.Time.month:
            return Universe.Unchanged
        
        #2. Update self.lastMonth with current month to make sure only process once per month
        self.lastMonth = algorithm.Time.month

        #3. Sort symbols by dollar volume and if they have fundamental data, in descending order
        sortedByDollarVolume = sorted([x for x in coarse if x.HasFundamentalData], 
                                      key=lambda x: x.DollarVolume, reverse=True)
        
        #4. Return the top 100 Symbols by Dollar Volume 
        return [x.Symbol for x in sortedByDollarVolume][:100]
