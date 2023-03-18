# Understanding Coarse Fundamental Objects
## Coarse Fundamental Objects
The **CoarseSelectionFilter** takes a parameter **coarse**. Coarse is an array of CoarseFundamentalObjects:

    def CoarseSelectionFilter(self, coarse):
        # 'coarse' is an array of CoarseFundamental data.
        # CoarseFundamental has properties Symbol, DollarVolume and Price.
        coarse[0].Symbol
        coarse[0].DollarVolume
        coarse[0].Price

## Using the Coarse Selection Filter
The **CoarseSelectionFilter** function narrows the list of companies according to properties like price and volume. The filter needs to return a list of symbols. For example, we may want to narrow down our universe to liquid assets, or assets that pass a technical indicator filter. We can do all of this in the coarse selection function.

You can use the coarse fundamental data to create your own criteria ("factors") to perform your selection. Once you have your target criteria there are two key tools: sorting and filtering. Sorting lets you take the top and/or bottom ranked symbols according to your criteria, filtering allows you to narrow your selection range to eliminate some assets. In python this is accomplished by sort and list selection methods. 

    # Use the sorted method to get keys in ascending order (greatest to least in DollarVolume)
    sortedByDollarVolume = sorted(coarse, key=lambda c: c.DollarVolume, reverse=True) 
    
    # Get symbols from your sorted list with a price more than $5 per share  
    symbols_by_price = [c.Symbol for c in sortedByDollarVolume if c.Price > 5]
    # Get the top 10 symbols 
    symbols_by_price[:10]

When you return a symbol from the **CoarseSelectionFilter**, LEAN automatically subscribes to these symbols and adds them to our algorithm.