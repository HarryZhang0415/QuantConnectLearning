# Sector Weighting Portfolio Construction
## Portfolio Construction Basics
Portfolio construction models (PCM) seek to generate targets for trade execution systems. These Portfolio Targets come from the Insights provided by the Alpha model.

## Sector Weighting Portfolio Construction Model

The Sector Weighting Portfolio Construction Model (SWPCM) performs a specific kind of portfolio construction where capital assigned to each sector is fixed. This minimizes risk exposure to a specific sector. The SWPCM needs to be used with a universe which selects assets based on fundamental data.

    # Default methods in the SWPCM class
    class SectorWeightingPortfolioConstructionModel(EqualWeightingPortfolioConstructionModel):
        def DetermineTargetPercent():
            pass
        def OnSecuritiesChanged():
            pass

In the SWPCM, insights for equities in a universe are grouped by their industry sector. Each grouping is assigned an equal percentage of total portfolio value. Each active sector in the universe is assigned equal weight.

## Inheritance from Equal Weighting Portfolio Construction

The SWPCM derives from the Equal Weighting Portfolio Construction Model (EWPCM). The coding simplification allows us to inherit most of the methods from the base class and only implement the **DetermineTargetPercent()** method.

The **DetermineTargetPercent()** method generates a dictionary of insights with the weight of the buying power to be assigned. The underlying classes of the EWPCM handle creating portfolio targets from those allocations.

## Rebalancing Periods

The **rebalance** parameter sets the rebalancing period of the SWPCM. The parameter accepts a timedelta, function, or **Resolution** object, which indicates the period between rebalancing.

When passing arguments to the underlying class, you use Python's **super()** function prefix, which provides access to the methods in the base class.

    # Pass in a rebalance argument into the underlying class
    def __init__(self, rebalance):
        super().__init__(rebalance)