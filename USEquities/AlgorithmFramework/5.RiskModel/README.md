# Risk Model

The Risk Management Model manages real-time market and portfolio risk. There are many potential applications for a risk model. For example, it may be used to ensure we are properly diversified or that we're limiting our drawdown.

## Data Flow: Risk Models
![Data Flow: Risk Models](https://cdn.quantconnect.com/i/tu/RiskModel3.jpg)
The Risk Management model receives an array of Portfolio Targets, manages risk on the PortfolioTarget collection and returns final risk adjusted portfolio targets to the Execution Model. Only the changed targets are delivered back.

## Setting a Risk Model
We set a risk management model in our **Initialize()** method.

    def Initialize(self):
        # Set the Risk Management Model to 2% MaximumDrawdown  
        self.SetRiskManagement(MaximumDrawdownPercentPerSecurity(0.02))

The **MaximumDrawdownPercentPerSecurity** class seeks to mitigate portfolio risk by limiting the drawdown of a specific asset. Drawdown is the loss incurred from the peak value of an asset to the trough. The model is created with the maximum allowed drawdown per security.