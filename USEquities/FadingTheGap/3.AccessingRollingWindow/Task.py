'''
Task Objectives
We will use our rolling window to decide when to place an order in the OpeningBar method.

If our window is not full yet use return to wait for tomorrow.
Calculate the change in overnight price using index values from our rolling window (ie. today's open - yesterday's close). Save the value to delta.
If delta is less than -$0.9, SetHoldings() to 100% TSLA.
'''

class FadingTheGap(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2017, 11, 1)
        self.SetEndDate(2018, 7, 1)
        self.SetCash(100000) 
        self.AddEquity("TSLA", Resolution.Minute)
        
        self.Schedule.On(self.DateRules.EveryDay(), self.TimeRules.BeforeMarketClose("TSLA", 0), self.ClosingBar) 
        self.Schedule.On(self.DateRules.EveryDay(), self.TimeRules.AfterMarketOpen("TSLA", 1), self.OpeningBar)
        self.Schedule.On(self.DateRules.EveryDay(), self.TimeRules.AfterMarketOpen("TSLA", 45), self.ClosePositions) 
        
        self.window = RollingWindow[TradeBar](2)
        
    def ClosingBar(self):
        self.window.Add(self.CurrentSlice["TSLA"])
    
    def OpeningBar(self):
        if "TSLA" in self.CurrentSlice.Bars:
            self.window.Add(self.CurrentSlice["TSLA"])
        
        #1. If our window is not full use return to wait for tomorrow
        if not self.window.IsReady:
            return
        
        #2. Calculate the change in overnight price
        delta = self.window[0].Price - self.window[1].Price
        
        #3. If delta is less than -$0.9, SetHoldings() to 100% TSLA
        if delta < -0.9:
            self.SetHoldings("TSLA", 1)
        
    def ClosePositions(self):
        self.Liquidate()
    
