'''
Task Objectives
Let's trade SPY and BND. In this task, we will set up a manual universe that takes a list of the two symbols.

Create two symbol objects, SPY and BND and save them to the self.symbols list. Both securities are an Equity security type and in the USA market.
Set the resolution of the universe assets to daily resolution.
Use self.SetUniverseSelection(), to set a ManualUniverseSelectionModel() initialized with the self.symbols list.
'''

class FrameworkAlgorithm(QCAlgorithm):
    
    def Initialize(self):

        self.SetStartDate(2013, 10, 1)   
        self.SetEndDate(2013, 12, 1)    
        self.SetCash(100000)           
        
        #1. Create a SPY and BND Symbol object that gets passed to the Universe Selection Model
        self.symbols = [Symbol.Create("SPY", SecurityType.Equity, Market.USA), 
                        Symbol.Create("BND", SecurityType.Equity, Market.USA)]
        #2. Set the resolution of the universe assets to daily resolution
        self.UniverseSettings.Resolution = Resolution.Daily
        #3. Set a universe using self.SetUniverseSelection(), and pass in a ManualUniverseSelectionModel() 
        self.SetUniverseSelection(ManualUniverseSelectionModel(self.symbols))
        # initialized with the symbols list
        
        self.SetAlpha(NullAlphaModel())
        self.SetPortfolioConstruction(NullPortfolioConstructionModel())
        self.SetRiskManagement(NullRiskManagementModel())
        self.SetExecution(NullExecutionModel())
    
