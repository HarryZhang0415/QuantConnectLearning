'''
Task Objectives
Let's implement a sector weighted strategy. We'll build upon a pre-defined coarse selection method, which passes in 100 of the top securities sorted by dollar volume into our fine filter.

In our SelectFine() method we'll narrow down our universe to securities from the technology, financial services, and consumer goods sectors.

# Access the sector codes
MorningstarSectorCode.FinancialServices
MorningstarSectorCode.ConsumerDefensive
MorningstarSectorCode.Technology
We filter our universe of assets by sector code in our FundamentalUniverseSelectionModel's SelectFine() method. Then we'll sort for the top securities by market capitalization.

# Example: filter and sort assets for the top 30 energy assets by Market Cap 
filtered = [x for x in fine if x.AssetClassification.MorningstarSectorCode == MorningstarSectorCode.Energy]
self.energy = sorted(filtered, key=lambda f: f.MarketCap, reverse=True)[:30]
Set an instance of MyUniverseSelectionModel using self.SetUniverseSelection().
Save the top 3 securities sorted by MarketCap for the technology sector to the variable self.technology.
Save the top 2 securities sorted by MarketCap for the financial services sector to the variable self.financialServices.
Save the top 1 securities sorted by MarketCap for the consumer defensive sector to the variable self.consumerDefensive.
'''

from datetime import timedelta
from AlgorithmImports import *
from QuantConnect.Data.UniverseSelection import * 
from Selection.FundamentalUniverseSelectionModel import FundamentalUniverseSelectionModel

class SectorBalancedPortfolioConstruction(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2016, 12, 28) 
        self.SetEndDate(2017, 3, 1) 
        self.SetCash(100000) 

        self.UniverseSettings.Resolution = Resolution.Hour
        #1. Set an instance of MyUniverseSelectionModel using self.SetUniverseSelection
        self.SetUniverseSelection(MyUniverseSelectionModel())
        
        self.SetAlpha(ConstantAlphaModel(InsightType.Price, InsightDirection.Up, timedelta(1), 0.025, None))
        self.SetExecution(ImmediateExecutionModel())

class MyUniverseSelectionModel(FundamentalUniverseSelectionModel):

    def __init__(self):
        super().__init__(True, None)

    def SelectCoarse(self, algorithm, coarse):
        filtered = [x for x in coarse if x.HasFundamentalData > 0 and x.Price > 0]
        sortedByDollarVolume = sorted(filtered, key=lambda x: x.DollarVolume, reverse=True)
        return [x.Symbol for x in sortedByDollarVolume][:100]

    def SelectFine(self, algorithm, fine):
        #2. Save the top 3 securities sorted by MarketCap for the Technology sector to the variable self.technology
        filtered = [x for x in fine if x.AssetClassification.MorningstarSectorCode == MorningstarSectorCode.Technology]
        self.technology = sorted(filtered, key=lambda x: x.MarketCap, reverse=True)[:3]

        #3. Save the top 2 securities sorted by MarketCap for the Financial Services sector to the variable self.financialServices
        filtered = [x for x in fine if x.AssetClassification.MorningstarSectorCode == MorningstarSectorCode.FinancialServices]
        self.financialServices = sorted(filtered, key=lambda x: x.MarketCap, reverse=True)[:2]
        
        #4. Save the top 1 securities sorted by MarketCap for the Consumer Goods sector to the variable self.consumerDefensive
        filtered = [x for x in fine if x.AssetClassification.MorningstarSectorCode == MorningstarSectorCode.ConsumerDefensive]
        self.consumerDefensive = sorted(filtered, key=lambda x: x.MarketCap, reverse=True)[:1]
        
        return [x.Symbol for x in self.technology + self.financialServices + self.consumerDefensive]

