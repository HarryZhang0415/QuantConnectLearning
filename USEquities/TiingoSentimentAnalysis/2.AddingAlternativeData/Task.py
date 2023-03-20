'''
Task Objectives
In our Alpha Model, request TiingoNews data for Nike and Apple. Then access TiingoNews object descriptions and assign each description a sentiment score.

Each TiingoNews object represents one news article. We access TiingoNews object properties by iterating through each article in news.Values from the Update() method.

In our Alpha Model's OnSecuritiesChanged() method, when new assets are added to the universe, request news data for the assets and save to the variable newsAsset. We can use the following request:
newsAsset = algorithm.AddData(TiingoNews, security.Symbol)
In our Alpha Model's Update() method, access TiingoNews with our Get() method and save to the variable news.
news = data.Get(TiingoNews)
In our Update() method, iterate through the article descriptions, convert the text to lowercase and split the descriptions up into a list of words. Save to the variable words.
# Access the values in a TiingoNews object
for article in news.Values:
    # Access the description property
    words = article.Description.lower().split(" ")
In our Update() method, assign a self.wordScore to our list of words if the word is in our self.wordScore dictionary. Sum up the scores of all the words in an article and save to the variable self.score.
'''

from QuantConnect.DataSource import *
from datetime import datetime, timedelta
import numpy as np

class TiingoNewsSentimentAlgorithm(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2016, 11, 1)
        self.SetEndDate(2017, 3, 1)  
        symbols = [Symbol.Create("AAPL", SecurityType.Equity, Market.USA), 
        Symbol.Create("NKE", SecurityType.Equity, Market.USA)]
        self.SetUniverseSelection(ManualUniverseSelectionModel(symbols))
        self.SetAlpha(NewsSentimentAlphaModel())
        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel()) 
        self.SetExecution(ImmediateExecutionModel()) 
        self.SetRiskManagement(NullRiskManagementModel())
        
class NewsSentimentAlphaModel(AlphaModel):
    
    def __init__(self):
        self.newsData = {} 
        
        # Assign polarity scores to words
        self.wordScores = {
            "bad": -0.5, "good": 0.5, "negative": -0.5, 
            "great": 0.5, "growth": 0.5, "fail": -0.5, 
            "failed": -0.5, "success": 0.5, "nailed": 0.5,
            "beat": 0.5, "missed": -0.5, "profitable": 0.5,
            "beneficial": 0.5, "right": 0.5, "positive": 0.5, 
            "large":0.5, "attractive": 0.5, "sound": 0.5, 
            "excellent": 0.5, "wrong": -0.5, "unproductive": -0.5, 
            "lose": -0.5, "missing": -0.5, "mishandled": -0.5, 
            "un_lucrative": -0.5, "up": 0.5, "down": -0.5,
            "unproductive": -0.5, "poor": -0.5, "wrong": -0.5,
            "worthwhile": 0.5, "lucrative": 0.5, "solid": 0.5
        } 
            
    def Update(self, algorithm, data):

        insights = []
        # 2. Access TiingoNews and save to the variable news
        news = data.Get(TiingoNews)
        
        for article in news.Values:
            # 3. Iterate through the article descriptions and save to the variable words
            # convert text to lowercase, and split the descriptions into a list of words
            words = article.Description.lower().split(" ")
            
            # 4. Assign a self.wordScore to the word if the word exists 
            # in self.wordScores and save to the variable self.score 
            self.score = sum([self.wordScores[word] for word in words 
                              if word in self.wordScores])
        return insights
    
    def OnSecuritiesChanged(self, algorithm, changes):

        for security in changes.AddedSecurities:
            # 1. When new assets are added to the universe
            # request news data for the assets and save to variable newsAsset
            newsAsset = algorithm.AddData(TiingoNews, security.Symbol)
            
