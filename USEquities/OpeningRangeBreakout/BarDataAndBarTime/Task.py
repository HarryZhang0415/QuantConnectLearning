"""
Task Objectives
Let's save the first bar of the day to use it's range later for trading sigals.

Save the first bar of the trading day to the class variable: self.openingBar. The first bar starts at 9:30am ET and ends at 10:00am ET.
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
        pass
        
    def OnDataConsolidated(self, bar):
        #1. Check the time, we only want to work with the first 30min after Market Open
            #2. Save one bar as openingBar 
        if bar.Time.hour == 9 and bar.Time.minute == 30:
            # Save the first bar of the trading day 
            self.openingBar = bar 
        
        # if bar.EndTime.hour == 10 and bar.EndTime.minute == 0:
        #     self.openingBar = bar
