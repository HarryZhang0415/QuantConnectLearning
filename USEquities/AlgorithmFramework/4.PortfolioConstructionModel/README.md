# Portfolio Construction Model

The Portfolio Construction Model takes in an array of Insights and calculates the number of shares per asset to hold.

## Data Flow: Portfolio Construction Model
![Data Flow: Portfolio Construction Model](https://cdn.quantconnect.com/i/tu/PortfolioConstructionModel3.jpg "Data Flow: Portfolio Construction Model")

The Portfolio Construction Model receives Insight objects from the Alpha Model and uses them to create **PortfolioTarget** objects for the Execution Model. A **PortfolioTarget** is a quantity of shares of the asset we'd like to eventually hold.

## Setting a Portfolio Model
We set our Portfolio Model in our **Initialize()** method.

    def Initialize(self):
        # Set the Portfolio Model to an Equal Weighting Portfolio Construction Model 
        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel())

One simple existing portfolio model we can use is the Equal Weighting Portfolio Construction Model. It assigns an equal share of the portfolio to insights currently active. When an insight period ends the holdings in the asset will be liquidated. The model can be configured to rebalance at different periods to reduce churn. By default the model scans for expired insights daily.