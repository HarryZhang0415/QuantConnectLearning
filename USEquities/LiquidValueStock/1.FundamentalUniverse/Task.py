'''
Task Objectives
We will buy the top 10 stocks and short the bottom 10 stocks in our universe. Let's start by creating the scaffolding for a custom universe class.

Create an instance of our LiquidValueUniverseSelectionModel. Set your Universe Settings to request hourly resolution data.
Add SelectCoarse() and SelectFine() methods to the Universe model class with proper parameters
'''

from AlgorithmImports import *
from Selection.FundamentalUniverseSelectionModel import FundamentalUniverseSelectionModel
class LiquidValueStocks(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2016, 10, 1)
        self.SetEndDate(2017, 10, 1)
        self.SetCash(100000)
        self.AddAlpha(NullAlphaModel())
        
        #1. Create an instance of our LiquidValueUniverseSelectionModel and set to hourly resolution
        self.AddUniverseSelection(LiquidValueUniverseSelectionModel())
        self.UniverseSettings.Resolution = Resolution.Hour
        
        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel())
        self.SetExecution(ImmediateExecutionModel())
        
        
# Define the Universe Model Class
class LiquidValueUniverseSelectionModel(FundamentalUniverseSelectionModel):
    
    def __init__(self):
        super().__init__(True, None)
    
    #2. Add an empty SelectCoarse() method with its parameters
    def SelectCoarse(self, algorithm, coarse):
        return Universe.Unchanged
    
    #2. Add an empty SelectFine() method with is parameters    
    def SelectFine(self, algorithm, fine):
        return Universe.Unchanged

