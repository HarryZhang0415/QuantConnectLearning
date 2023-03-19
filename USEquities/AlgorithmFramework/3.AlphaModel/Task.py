'''
Task Objectives
Let's create an Alpha Model that uses two 14-day momentum indicators. The model will emit an Insight every day signaling Up for the asset with the strongest momentum.

In def OnSecuritiesChanged(), initialize a 14-day momentum indicator for each symbol. Store it in the list named self.mom.
In def Update(), sort the dictionaries of momentum indicators in descending order and save them to ordered. def Update(self, algorithm, data):
    # Sort our list of dictionaries by indicator in descending order 
    ordered = sorted(self.mom, key=lambda kv: kv["indicator"].Current.Value, reverse=True)
Return a group of insights from def Update(), emitting InsightDirection.Up for the first item of ordered, and InsightDirection.Flat for the second.
'''

from datetime import timedelta

class MOMAlphaModel(AlphaModel):
    
    def __init__(self):
        self.mom = []
      
    def OnSecuritiesChanged(self, algorithm, changes):
        
        # 1. Initialize a 14-day momentum indicator for each symbol
        for security in changes.AddedSecurities:
            symbol = security.Symbol
            self.mom.append({"symbol":symbol, "indicator":algorithm.MOM(symbol, 14, Resolution.Daily)})
        
    def Update(self, algorithm, data):

        #2. Sort the list of dictionaries by indicator in descending order
        ordered = sorted(self.mom, key=lambda kv: kv["indicator"].Current.Value, reverse=True)
        
        #3. Return a group of insights, emitting InsightDirection.Up for the first item of ordered, and InsightDirection.Flat for the second
        return Insight.Group([
            # Create a grouped insight
            Insight.Price(ordered[0]["symbol"], timedelta(1), InsightDirection.Up), 
            Insight.Price(ordered[1]["symbol"], timedelta(1), InsightDirection.Flat)
        ])
        
class FrameworkAlgorithm(QCAlgorithm):
    
    def Initialize(self):

        self.SetStartDate(2013, 10, 1)   
        self.SetEndDate(2013, 12, 1)   
        self.SetCash(100000)           
        symbols = [Symbol.Create("SPY", SecurityType.Equity, Market.USA), Symbol.Create("BND", SecurityType.Equity, Market.USA)]
        self.UniverseSettings.Resolution = Resolution.Daily
        self.SetUniverseSelection(ManualUniverseSelectionModel(symbols))

        # Call the MOMAlphaModel Class 
        self.SetAlpha(MOMAlphaModel())

        self.SetPortfolioConstruction(NullPortfolioConstructionModel())
        self.SetRiskManagement(NullRiskManagementModel())
        self.SetExecution(NullExecutionModel())
    

    
