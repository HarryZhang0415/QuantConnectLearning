# Grouping Data with Classes
## The 200-50 EMA Momentum Strategy
An exponential moving average (EMA) is a technical analysis tool. We can calculate averages of asset price for any time period.

The momentum strategy hypothesis is that stocks that have performed well in the past will continue to perform well. The EMA Momentum Universe selects stocks based on their fast and slow moving average values. An **ExponentialMovingAverage()** class is initialized with a number of bars. Its period is that bar count, multiplied by the period of the bars used.

## Creating Classes
So far our algorithms have all been part of one class. We can create additional classes as a way to group together variables for our universe selection and update any indicators all in a few lines of code. We create another class so each class focuses on one problem, this is known as "Separation of Concerns".

## Initializing Class Objects
Classes can set a constructor to initialize members of the class.

    # Create a class to group our indicators
    class SelectionData:
        # Set the constructer __init__ that takes the parameter self
        def __init__(self): 
            # Save the indicator to self.ema 
            self.slow = ExponentialMovingAverage(200)
        
Methods can group code and provide a clean way to check our indicators are ready. For universes it is convenient to check if our indicators are ready with the **IsReady** property:

    # Create a class method called is_ready
    class SelectionData:
        def is_ready(self):
            # Return the IsReady property 
            return self.slow.IsReady
    
We could also use a method to group updating indicators as demonstrated below. The benefits of this abstraction are more obvious with more complex examples.

    # Create a class method called update that takes the parameters self, time, price
    class SelectionData:
        def update(self, time, price):
            #Use the Update property to get the time and price for our indicators 
            self.fast.Update(time, price)
            self.slow.Update(time, price)

