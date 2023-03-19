# Applying Class In Universe
## Universes and Dictionaries
Let's create a **SelectionData** for every security in our universe, and store it in a dictionary to quickly access their methods.
Initializing a Dictionary

    # Initialize a dictionary called averages
    self.averages = {}

Adding to a Dictionary, Checking if an Item is in Dictionary

Dictionaries are a way of storing data which you can look up later with a "key". To perform EMA-universe selection on every security we'll need a **SelectionData** for every Symbol in our universe.

We can check if an item exists in a dictionary with in. We should check if it exists before creating a new copy:

    # check if the object is already in the dictionary. 
    if symbol not in self.averages:
        # Add the new SelectionData to the key 
        self.averages[symbol] = SelectionData()

## Accessing Dictionary Items
You can access and use dictionary items with braces/brackets. Using braces you can look up the specific Symbol and find the right SelectionData value.

    # e.g. Accessing a method and pass in parameters
    self.averages[symbol].update(self.Time, coarse.AdjustedPrice)
    # e.g. Accessing property of class, as a dictionary item
    if self.averages[symbol].fast > self.averages[symbol].slow:
        # Access dictionary methods with braces using "dot notation"
        if self.averages[symbol].is_ready():
            selected.append(symbol)