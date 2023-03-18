"""
Task Objectives
The breakout signal is strongest in the morning. Let's use a scheduled event to close our position each day at 13:30 ET.

Create an event handler for our scheduled event named def ClosePositions(self):
Inside your ClosePositions function set self.openingBar to None and liquidate TSLA.
Create a scheduled event triggered at 13:30 ET calling the ClosePositions function.
"""

class OpeningRangeBreakout(QCAlgorithm):
    
    openingBar = None 
    
    def Initialize(self):
        self.SetStartDate(2018, 7, 10)  
        self.SetEndDate(2019, 6, 30)  
        self.SetCash(100000)
        self.AddEquity("TSLA", Resolution.Minute)
        self.Consolidate("TSLA", timedelta(minutes=30), self.OnDataConsolidated)
        
        #3. Create a scheduled event triggered at 13:30 calling the ClosePositions function
        self.Schedule.On(self.DateRules.EveryDay("TSLA"), self.TimeRules.At(13,30), self.ClosePositions)
        
    def OnData(self, data):
        
        if self.Portfolio.Invested or self.openingBar is None:
            return
        
        if data["TSLA"].Close > self.openingBar.High:
            self.SetHoldings("TSLA", 1)

        elif data["TSLA"].Close < self.openingBar.Low:
            self.SetHoldings("TSLA", -1)  
         
    def OnDataConsolidated(self, bar):
        if bar.Time.hour == 9 and bar.Time.minute == 30:
            self.openingBar = bar
    
    #1. Create a function named ClosePositions(self)
        #2. Set self.openingBar to None, and liquidate TSLA 
    
    def ClosePositions(self):
        self.openingBar = None
        self.Liquidate("TSLA")