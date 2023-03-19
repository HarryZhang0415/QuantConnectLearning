# Creating Scheduled Events
## Fading The Gap
The difference between the close price of the previous day and the opening price of the current day is referred to as a gap. Fading the gap is a strategy that monitors for a large gap down and buys stock assuming it will rebound.

## Using Scheduled Events
Scheduled events trigger a method at a specific date and time. Scheduled events have three parameters: a **DateRule**, a **TimeRule**, and an action parameter. Our action parameter should be set to the name of a method.

Setting Event Time

Our time rules **AfterMarketOpen** and **BeforeMarketClose** take a *symbol*, and *minute* period. Both trigger an event a for a specific symbol's market hours.

    # Trigger event 1 min after SPY market open (9.31am).
    self.TimeRules.AfterMarketOpen("SPY", 1) 
    # Trigger event at SPY market close (4pm).
    self.TimeRules.BeforeMarketClose("SPY", 0) 

Setting Event Action

    def Initialize(self):
        # Schedule an event to fire every trading day for a security.
        # Remember to schedule events in initialize of your algorithm.
        # The time rule here tells the algorithm to fire 1 minute after TSLA's market open
        self.Schedule.On(self.DateRules.EveryDay(),
                        self.TimeRules.AfterMarketOpen("TSLA", 1),
                        self.FadeTheGap)
    def FadeTheGap(self):
        pass

You must schedule events in your algorithm **Initialize** method.