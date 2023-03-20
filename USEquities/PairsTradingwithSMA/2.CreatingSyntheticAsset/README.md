# Creating a Synthetic Asset
## What is a Synthetic Asset?

The difference in price between our pair of assets is called the spread.

![Spread](https://cdn.quantconnect.com/i/tu/pair_of_assets_example3.png)

We can think of the spread as a synthetic asset, a combination of assets that have the financial effect becoming a brand new asset.

The spread can be shown as its own time series. The plot below shows the difference between assets.

![New Asset](https://cdn.quantconnect.com/i/tu/spread_pairs_trading3.png)

## Creating Our Alpha Model
To model this new "synthetic asset" we create a spread indicator to track its value. Our new indicator will live inside our Pairs Trading Alpha Model.

    # Create an instance of the Alpha Model
    self.AddAlpha(PairsTradingAlphaModel())

The **OnSecuritiesChanged()** method is used to define the pair to trade. We calculate our spread in our **Update()** method as the price difference between the two assets.

    def Update(self, algorithm, data):
        # Calculate the price difference
        spread = self.pair[1].Price - self.pair[0].Price

## Updating Our Pairs
We set our pairs in the OnSecuritiesChanged() method.

    def OnSecuritiesChanged(self, algorithm, changes):
        self.pair = [x for x in changes.AddedSecurities]

