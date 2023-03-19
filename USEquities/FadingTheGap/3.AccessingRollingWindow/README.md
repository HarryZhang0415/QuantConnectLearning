# Accessing a Rolling Window
## Checking if the Window Is Ready
Our window is not full when we first create it. QuantConnect provides a shortcut to check the if the rolling window is full("ready"): **window.IsReady** which will return true when all slots of the window have data.

    # If the window is not ready
    # return and wait 
    if not self.window.IsReady:
        return

## Accessing Rolling Window Data
The object in the window with index [0] refers to the most recent item. The length-1 in the window is the oldest object.

    # In a rolling window with len=2
    # access the latest object
    # from the rolling window with index 0 
    self.window[0]
    # In a rolling window with len=2
    # access the last object
    # from the rolling window with index 1 
    self.window[1]