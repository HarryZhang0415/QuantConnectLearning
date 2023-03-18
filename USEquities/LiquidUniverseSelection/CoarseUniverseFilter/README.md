# Setting Up a Coarse Universe Filter
## Introduction to Universe Selection
We use universe selection to algorithmically reduce the number of assets added to our algorithm (the investment “universe”). We want to choose our assets with formulas, not by manually selecting our favorite assets.
## Selection Bias
Universe selection helps us avoid selection bias by algorithmically choosing our assets for trading. Selection bias is introduced when the asset selection is influenced by personal or non-random decision making, and often results in selecting winning stocks based on future knowledge.
## Coarse Selection
We can add a universe with the method **self.AddUniverse()**

    # Pass the filter function into AddUniverse in your Initializer
    def Initialize(self):
        self.AddUniverse(self.CoarseSelectionFilter)
    # Create a filter function    
    def CoarseSelectionFilter(self, coarse):
        pass

The method requires a filter function **CoarseSelectionFilter** which is passed an array of coarse data representing all stocks active on that trading day. Assets selected by our filter are automatically added to your algorithm in minute resolution.

## Universe Unchanged
If we don't have specific filtering instructions for our universe, we can use **Universe.Unchanged** which specifies that universe selection should not make changes on this iteration.

    # Create a filter function that currently does not change the universe 
    def CoarseSelectionFilter(self, coarse):
        return Universe.Unchanged

