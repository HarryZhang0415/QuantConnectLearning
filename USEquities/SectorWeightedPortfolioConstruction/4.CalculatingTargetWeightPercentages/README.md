# Calculating Target Weight Percentages
## Sector & Asset Target Weight Allocation
The Sector Weighted Portfolio Construction Model (SWPCM) assigns each sector a fixed capital allocation. The capital assigned to each sector depends on the number of sectors in your universe.

The default SWPCM assumes a 1.0 leverage, so the sector buying power is a fraction of 1.0.

The capital assigned to each asset in the sector, is a fraction of the sector capital allocation.

## Using Active Insights

The Equal Weighting Portfolio Construction Model (EWPCM) base class tracks the currently active insights from the algorithm alpha model and provides a list of currently active signals to the **DetermineTargetPercent()** method. Active insights are insights from the alpha model, which have not expired and should receive a target allocation.

## Calculating Security Target Allocations

The SWPCM determines the security allocation based on the sector capital allocation divided by the number of securities in that sector. For example, the Consumer Defensive sector has 33% buying power allocation, and only 1-security selected which should receive the full 33% buying power allocation.

## Determine Target Percent Method

The **DetermineTargetPercent()** method returns percent targets for each insight in the form of a dictionary of active insights and percent targets. Through inheritance from the EWPCM, the percent target is turned into a target number of shares for the execution model.

The portfolio percent target for each insight in the sector is calculated by multiplying the insight direction by the sector percent target.