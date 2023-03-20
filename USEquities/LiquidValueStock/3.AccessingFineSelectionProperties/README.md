# Accessing Fine Selection Properties
The symbols that enter our fine universe are further filtered based on fundamental data.

## Accessing Fine Selection Properties
Each ticker has 900 fundamental data objects. The object's categories are: **CompanyReferences**, **SecurityReferences**, **FinancialStatements**, EarningsReports, OperationRatio, EarningRatios, ValuationRatios. Find the full library of objects [here](https://www.quantconnect.com/docs/v2/writing-algorithms/datasets/morningstar/us-fundamental-data#06-Data-Point-Attributes).

Like coarse universe selection, we filter our fine universe of symbols based on "fine" objects. All fundamental data objects are updated once per month and a ticker's financial ratios are updated daily. We can then filter and sort based on the fundamental data values.

    # Examples of sorted fundamental data

    # Sort earnings yields per share where a high earning yield indicates an undervalued stock
    sortedByYields = sorted(fine, key=lambda f: f.ValuationRatios.EarningYield, reverse=True)

    # Sort 1 year high PE Ratios where a low PE Ratio can indicate an undervalued stock 
    sortedByPE = sorted(fine, key=lambda f: f.ValuationRatios.PERatio1YearHigh, reverse=False)

We can take an index slice of our sorted list of fine symbols to return as our fine universe.

    def SelectFine(self, algorithm, fine):
        # Take top 10 most profitable stocks -- and bottom 10 least profitable stocks.
        self.universe = sortedByYields[:10] + sortedByYields[-10:]
        # Make sure to return the symbol objects
        return [f.Symbol for f in self.universe]
