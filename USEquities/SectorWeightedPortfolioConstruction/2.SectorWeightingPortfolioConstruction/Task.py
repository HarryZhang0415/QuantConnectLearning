'''
Task Objectives
In the previous task, we selected the universe of assets available. To trade a portfolio that is equally weighted by sector, we'll need to generate equally weighted Portfolio Targets. Let's set up our constructor to track the number of assets in a sector.

Set an instance of the SectorWeightingPortfolioConstructionModel using self.SetPortfolioConstruction
Edit the class constructor to accept a rebalance parameter, defaulting to Resolution.Daily
Initialize the underlying class constructor by passing through rebalance to super().__init__().
In the constructor, initialize an empty dictionary self.symbolBySectorCode. We'll use it to group the securities by sector code.
'''

from datetime import timedelta
from AlgorithmImports import *
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
        # 1. Set an instance of the MySectorWeightingPortfolioConstructionModel using self.SetPortfolioConstruction
        self.SetPortfolioConstruction(MySectorWeightingPortfolioConstructionModel())
        
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

    # 2. In the constructor, pass in the rebalance parameter and set it to daily resolution
    def __init__(self, rebalance = Resolution.Daily):
        # 3. Initialize the underlying class by passing it through
        super().__init__()

        # 4. Initialize an empty dictionary self.symbolBySectorCode to group the securities by sector code
        self.symbolBySectorCode = {}

