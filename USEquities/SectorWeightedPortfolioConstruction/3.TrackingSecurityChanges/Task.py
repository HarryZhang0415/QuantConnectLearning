'''
Task Objectives
Let's use OnSecuritiesChanged events to track how many securities are in each sector. As securities are added, add the security symbol to the list for that sector in the self.symbolBySectorCode dictionary.

In this implementation, we'll want the dictionary keys to be sectorCode and the values to be lists of the security symbols. We'll use this mapping to determining sector weight allocations in the next task.

We can check if the asset symbol is in our storage with an if not in statement and use the append() function if it is not already there.

To remove a value at a specific key if the key exists in storage, we can use the remove(key) function that removes and returns the last value from the dictionary, returning default if none exists in storage.

When new assets are added to the universe, save the sector code for each security to the variable sectorCode.
If the sectorCode is not in the self.symbolBySectorCode dictionary, create a new list and append the symbol to the list, keyed by sectorCode, in the self.symbolBySectorCode dictionary.
if sectorCode not in self.symbolBySectorCode:
    self.symbolBySectorCode[sectorCode] = list()
self.symbolBySectorCode[sectorCode].append(security.Symbol)
When assets are removed from the universe, save the sector code for each security to sectorCode
Remove the symbol from the sector-symbol list stored in the dictionary. First check if the sectorCode is in the self.symbolBySectorCode dictionary, then check if the symbol is in the dictionary's list, then use the remove() method to remove the symbol object from the dictionary.
'''

from datetime import timedelta
from QuantConnect.Data.UniverseSelection import * 
from Selection.FundamentalUniverseSelectionModel import FundamentalUniverseSelectionModel
from Portfolio.EqualWeightingPortfolioConstructionModel import EqualWeightingPortfolioConstructionModel

class SectorBalancedPortfolioConstruction(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2016, 12, 28) 
        self.SetEndDate(2017, 3, 1) 
        self.SetCash(100000) 
        self.UniverseSettings.Resolution = Resolution.Hour
        self.SetUniverseSelection(MyUniverseSelectionModel())
        self.SetAlpha(ConstantAlphaModel(InsightType.Price, InsightDirection.Up, timedelta(1), 0.025, None))
        self.SetPortfolioConstruction(MySectorWeightingPortfolioConstructionModel(Resolution.Daily))
        self.SetExecution(ImmediateExecutionModel())

class MyUniverseSelectionModel(FundamentalUniverseSelectionModel):

    def __init__(self):
        super().__init__(True, None)

    def SelectCoarse(self, algorithm, coarse):
        filtered = [x for x in coarse if x.HasFundamentalData and x.Price > 0]
        sortedByDollarVolume = sorted(filtered, key=lambda x: x.DollarVolume, reverse=True)
        return [x.Symbol for x in sortedByDollarVolume][:100]

    def SelectFine(self, algorithm, fine):
        filtered = [f for f in fine if f.AssetClassification.MorningstarSectorCode == MorningstarSectorCode.Technology]
        self.technology = sorted(filtered, key=lambda f: f.MarketCap, reverse=True)[:3]
        filtered = [f for f in fine if f.AssetClassification.MorningstarSectorCode == MorningstarSectorCode.FinancialServices]
        self.financialServices = sorted(filtered, key=lambda f: f.MarketCap, reverse=True)[:2]
        filtered = [f for f in fine if f.AssetClassification.MorningstarSectorCode == MorningstarSectorCode.ConsumerDefensive]
        self.consumerDefensive = sorted(filtered, key=lambda f: f.MarketCap, reverse=True)[:1]
        return [x.Symbol for x in self.technology + self.financialServices + self.consumerDefensive]
        
class MySectorWeightingPortfolioConstructionModel(EqualWeightingPortfolioConstructionModel):

    def __init__(self, rebalance = Resolution.Daily):
        super().__init__(rebalance)
        self.symbolBySectorCode = dict()

    def OnSecuritiesChanged(self, algorithm, changes):
        
        for security in changes.AddedSecurities:
            #1. When new assets are added to the universe, save the Morningstar sector code 
            # for each security to the variable sectorCode
            sectorCode = security.Fundamentals.AssetClassification.MorningstarSectorCode
            
            # 2. If the sectorCode is not in the self.symbolBySectorCode dictionary, create a new list 
            # and append the symbol to the list, keyed by sectorCode in the self.symbolBySectorCode dictionary 
            if sectorCode not in self.symbolBySectorCode:
                self.symbolBySectorCode[sectorCode] = list()
            self.symbolBySectorCode[sectorCode].append(security.Symbol)
            
        for security in changes.RemovedSecurities:
            #3. For securities that are removed, save their Morningstar sector code to sectorCode
            sectorCode = security.Fundamentals.AssetClassification.MorningstarSectorCode
            
            #4. If the sectorCode is in the self.symbolBySectorCode dictionary
            if sectorCode in self.symbolBySectorCode:
                symbol = security.Symbol
                # If the symbol is in the dictionary's sectorCode list;
                if symbol in self.symbolBySectorCode[sectorCode]:
                    # Then remove the corresponding symbol from the dictionary
                    self.symbolBySectorCode[sectorCode].remove(symbol)
                
        # We use the super() function to avoid using the base class name explicity
        super().OnSecuritiesChanged(algorithm, changes)

