'''
Task Objectives
Use our SWPCM to allocate an equal buying power to each sector, and calculate the buying power percentage for each sector's insights.

First, extract the active insights for a specific sector, using the self.symbolBySectorCode dictionary generated in the previous task. Then calculate the percent of buying power to assign to each insight in the sector.

Finally, iterate through the insights and multiply the equal weight by the insight direction to return a target percent, and save as a value in self.result. Through inheritance, the target percent is turned into a target number of shares (Portfolio Targets) and delivered to the execution model.

In DetermineTargetPercent(), set the self.sectorBuyingPower before by dividing 1.0 by the length of self.symbolBySectorCode
Search for the active insights in a sector. Save to the variable self.insightsInSectorfor sector, symbols in self.dictionary.items():
    self.insightsInSector = [insight for insight in activeInsights if insight.Symbol in symbols] 
Divide the self.sectorBuyingPower by the length of self.insightsInSector to calculate the percent weight to assign the direction of the insight
For each insight in self.insightsInSector, calculate the target percentage weight and save it to self.result, indexed by the insight object. The allocation is calculated by multiplying the insight direction by the self.percent.
for insight in self.insightsInSector:
    self.result[insight] = insight.Direction * self.percent
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
        self.result = dict()

    def DetermineTargetPercent(self, activeInsights):
        #1. Set the self.sectorBuyingPower before by dividing one by the length of self.symbolBySectorCode
        self.sectorBuyingPower = 1 / len(self.symbolBySectorCode)
            
        for sector, symbols in self.symbolBySectorCode.items():
            #2. Search for the active insights in this sector. Save the variable self.insightsInSector
            self.insightsInSector = [insight for insight in activeInsights if insight.Symbol in symbols]
        
            #3. Divide the self.sectorBuyingPower by the length of self.insightsInSector to calculate the variable percent
            # The percent is the weight we'll assign the direction of the insight
            self.percent = self.sectorBuyingPower / len(self.insightsInSector)
        
            #4. For each insight in self.insightsInSector, assign each insight an allocation. 
            # The allocation is calculated by multiplying the insight direction by the self.percent 
            for insight in self.insightsInSector:
                self.result[insight] = insight.Direction * self.percent
        
        return self.result


    def OnSecuritiesChanged(self, algorithm, changes):
        for security in changes.AddedSecurities:
            sectorCode = security.Fundamentals.AssetClassification.MorningstarSectorCode
            if sectorCode not in self.symbolBySectorCode:
                self.symbolBySectorCode[sectorCode] = list()
            self.symbolBySectorCode[sectorCode].append(security.Symbol) 

        for security in changes.RemovedSecurities:
            sectorCode = security.Fundamentals.AssetClassification.MorningstarSectorCode
            if sectorCode in self.symbolBySectorCode:
                symbol = security.Symbol
                if symbol in self.symbolBySectorCode[sectorCode]:
                    self.symbolBySectorCode[sectorCode].remove(symbol)

        super().OnSecuritiesChanged(algorithm, changes)


