'''
Task Objectives
This lesson will use pre-selected pairs in a manual universe at hourly resolution with Pepsi "PEP" and Coca-Cola "KO" stocks. The stocks are likely cointegrated and have a price difference that is stationary. Let's add the symbols to our universe and set up the rest of our algorithm framework. In the Initialize() method:

Using the ManualUniverseSelectionModel(), add the symbols "PEP" and "KO".
Set UniverseSettings.Resolution to hourly resolution.
'''

from datetime import timedelta, datetime

class SMAPairsTrading(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2018, 7, 1)   
        self.SetEndDate(2019, 3, 31)
        self.SetCash(100000)
        
        #1. Using the ManualUniverseSelectionModel(), add the symbols "PEP" and "KO" 
        symbols = [Symbol.Create("PEP", SecurityType.Equity, Market.USA), 
                    Symbol.Create("KO", SecurityType.Equity, Market.USA)]
        self.SetUniverseSelection(ManualUniverseSelectionModel(symbols))
        #2. In Universe Settings, set the resolution to hour
        self.UniverseSettings.Resolution = Resolution.Hour
        
        self.AddAlpha(NullAlphaModel())
        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel())
        self.SetExecution(ImmediateExecutionModel())
        