# Creating a Consolidator
## Introduction

Opening range breakout uses a defined period of time to set a price-range, and trades on leaving that range. To achieve this we will start by consolidating the first 30 minutes of data.

## Consolidators

Consolidators are used to combine smaller data points into larger bars. We commonly use consolidators to create 5, 10 or 15-minute bars from minute data.

The **self.Consolidate()** method takes a **ticker**, **timedelta**, and **event handler**. It can also take a **CalendarType** or a **Resolution** parameter.

    # Receive consolidated data with a timedelta 
    # parameter and OnDataConsolidated event handler 
    self.Consolidate("SPY", timedelta(minutes=45), self.OnDataConsolidated)

    # Receive consolidated data with a CalendarType
    # parameter and OnDataConsolidated event handler 
    self.Consolidate("SPY", CalendarType.Weekly, self.OnDataConsolidated)

    # Receive consolidated data with a Resolution
    # parameter and OnDataConsolidated event handler 
    self.Consolidate("SPY", Resolution.Hour, TickType.Trade, self.OnDataConsolidated)

## Initializing Consolidators

**Consolidate** should be called in your **Initialize()** method so it is initialized only once. You must request data smaller than the bar you aim to consolidate. For example, it is not possible to consolidate daily data into minute bars.

## Event Handler Functions
Consolidators require an accompanying event handler to receive the output data. The consolidator event handlers are functions which are called when a new bar is created. We can name the event handler anything as long as it is passed into our **Consolidate** method.

    # Consolidators require an event handler function to recieve data
    def OnDataConsolidated(self, bar):
        # We can save the first bar as the currentBar
        self.currentBar = ...