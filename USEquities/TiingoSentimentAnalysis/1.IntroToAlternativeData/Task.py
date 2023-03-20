'''
Task Objectives
In this lesson, we will be exploring one of QuantConnect's data libraries, Tiingo's News Data for US Equities. Tiingo crawls the web for financial news articles and delivers each article in the form of a TiingoNews object. Tiingo's data library contains approximately 8,000-12,000 articles from each day since January, 1st 2014.

We will use TiingoNews data to implement an algorithm that emits insights to trade Nike and Apple based on news sentiment on the two companies.

In our Initialize() method, add an instance of our manual universe. To the universe, add "AAPL" and "NKE" symbols
In our Initialize() method, add an instance of our NewsSentimentAlphaModel() with self.SetAlpha()
Create a NewsSentimentAlphaModel class with Update() and OnSecuritiesChanged() methods
'''

from AlgorithmImports import *
class TiingoNewsSentimentAlgorithm(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2016, 11, 1)
        self.SetEndDate(2017, 3, 1)  
        
        #2. Add AAPL and NKE symbols to a Manual Universe 
        symbols = [Symbol.Create("AAPL", SecurityType.Equity, Market.USA),
                   Symbol.Create("NKE", SecurityType.Equity, Market.USA)]
        self.AddUniverseSelection(ManualUniverseSelectionModel(symbols))

        # 3. Add an instance of the NewsSentimentAlphaModel
        self.SetAlpha(NewsSentimentAlphaModel())
        
        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel()) 
        self.SetExecution(ImmediateExecutionModel()) 
        self.SetRiskManagement(NullRiskManagementModel())
        
# 4. Create a NewsSentimentAlphaModel class with Update() and OnSecuritiesChanged() methods
class NewsSentimentAlphaModel(AlphaModel):
    def __init__(self): 
        pass

    def Update(self, algorithm, data):
        return []

    def OnSecuritiesChanged(self, algorithm, changes):
        pass
