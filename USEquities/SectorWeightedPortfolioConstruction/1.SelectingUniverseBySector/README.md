# Selecting Universe By Sector
## Diversification of Investment Sectors
A sector balanced portfolio strategy invests in assets across industries. Its goal is to expose the portfolio to less risk from a specific sector and generate more robust returns through a variety of market conditions.

## MorningStar Asset Sector Classification Properties
We can use Morningstar fundamental data to select a universe of equities by sector. The asset classification data is stored in the AssetClassification property, with groupings by industry and sector.

Morningstar fundamental data maps equities to 11 asset sector classifications. Smaller industry groupings with similar operational characteristics make up these sector classifications. You can read more about Morningstar asset classifications here. We use the **MoringstarSectorCode** property to access sector classification codes.

## Universe Selection by Market Capitalization
A common way to sort assets is by market capitalization, the market value of outstanding shares for a publicly-traded company. Calculate market cap by multiplying the number of shares outstanding by the closing price per share. We access a company's market cap on the **FineFundamental** object.

    FineFundamental.MarketCap

