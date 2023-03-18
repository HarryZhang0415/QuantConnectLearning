"""
Task Objectives
The breakout point is when the price breaks past the high or low of the market opening range.
If we have already invested, or if the openingBar is None, exit OnData.
If the close price of TSLA is greater than the openingBar.High price, go 100% long on TSLA.
If the close price of TSLA is less than the openingBar.Low price, go 100% short on TSLA.
"""
class OpeningRangeBreakout(QCAlgorithm):
    
    openingBar = None 
    
    def Initialize(self):
        self.SetStartDate(2018, 7, 10)  
        self.SetEndDate(2019, 6, 30)  
        self.SetCash(100000)
        self.AddEquity("TSLA", Resolution.Minute)
        self.Consolidate("TSLA", timedelta(minutes=30), self.OnDataConsolidated)
        
    def OnData(self, data):
        
        #1. If self.Portfolio.Invested is true, or if the openingBar is None, return
        if self.Portfolio.Invested or self.openingBar is None:
            return
        
        #2. Check if the close price is above the high price, if so go 100% long on TSLA 
        
        if data["TSLA"].Close > self.openingBar.High:
            self.SetHoldings("TSLA", 1)

        #3. Check if the close price is below the low price, if so go 100% short on TSLA
        if data["TSLA"].Close < self.openingBar.High:
            self.SetHoldings("TSLA", -1)

    def OnDataConsolidated(self, bar):
        if bar.Time.hour == 9 and bar.Time.minute == 30:
            self.openingBar = bar
