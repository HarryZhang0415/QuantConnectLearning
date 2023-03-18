# Scheduling Events
## Scheduling Events

Scheduled events allow you to trigger code blocks for execution at specific times according to rules you set. We initialize scheduled events in the **Initialize** method so they are only executed once.

We use **self.Schedule.On()** to coordinate your algorithm activities and perform analysis at regular intervals while letting the trading engine take care of market holidays.

    # Coordinate algorithm activities with self.Schedule.On()
    self.Schedule.On(self.DateRules.EveryDay("SPY"), self.TimeRules.At(13,30), self.ClosePositions)

## Using Scheduling Helpers
Scheduled events need a **DateRules** and **TimeRules** pair to set a specific time, and an action that you want to complete. When the event is triggered the action block (or function) is executed. We include our asset ticker in our **EveryDay("ticker")** object to specifify that we are calling days there is data for the ticker. You can learn more in the documentation.

    # Trigger an event that occurs every day there is data for SPY 
    self.DateRules.EveryDay("SPY") 


## Liquidate
**Liquidate("ticker")** closes any open positions with a market order, and closes any open limit orders.

    def ClosePositions(self):
        self.openingBar = None
        self.Liquidate("TSLA")