# Customizing Universe Settings
## Universe Settings
You can control the settings of assets added by universe selection with the UniverseSettings helper. This mostly used to control the Resolution, Leverage and Data Normalization Mode of assets in your universe.

    self.UniverseSettings.Resolution
    self.UniverseSettings.Leverage
    self.UniverseSettings.FillForward
    self.UniverseSettings.MinimumTimeInUniverse
    self.UniverseSettings.ExtendedMarketHours

## Leverage with SetHoldings

Brokerages sometimes let clients borrow money to invest, this is known as leverage. When leverage is available you can purchase up to "Cash x Leverage" worth of stock.

**SetHoldings** calculates the number of shares to purchase, based on a fraction of your equity, and then places a market order for them. For example, if you have $10,000 cash, **SetHoldings("SPY", 1.0)** will attempt to purchase $10,000 of SPY. With a leverage of 2.0, you could use **SetHoldings("SPY", 2.0)** and purchase $20,000 of SPY, with $10,000 cash.

## Keeping a Cash Buffer

The market can quickly change price from the time you place the SetHoldings request to when the order is filled. If your portfolio allocations sum to exactly 100% orders may be rejected due to insufficient buying power. You should leave a buffer to account for market movements and fees. This is especially important with daily data where orders are placed overnight.

    # Set holdings to a percentage with a cash buffer 
    # Leverage 1.0: 10 Assets x 0.10 each => 100%, 0% buffer, fail.
    # Leverage 2.0: 10 Assets x 0.18 each => 180%, 20% buffer 
    self.SetHoldings(security.Symbol, 0.18)