# Framework Overview
## Introduction
The QC Algorithm Framework is the foundation for building a robust and flexible investment strategy. The framework architecture makes it simple to reuse code and provides the scaffolding for good algorithm design.

The framework is a system that connects the inputs and outputs of five models to ultimately deliver filled orders based on your strategy. The five steps of the system are universe selection, alpha creation, portfolio construction, risk management, and finally execution of trades.

## Data Flow

The data output of each module flows into the next predictably. Assets selected by the *Universe Selection Model* are fed into your *Alpha Model* to generate trade signals. The trade signals, or insights, are converted into Portfolio Targets by the *Portfolio Construction Model*. The Portfolio Targets hold a target share quantity we'd like the algorithm to hold. The *Risk Management Model* ensures our targets are still within safe risk parameters and adjusts the portfolio targets if required. To execute these targets efficiently the Execution model fills the targets efficiently over time.

## Separation of Concerns
Used together, the models handle the basic requirements of a trading algorithm, allowing you to focus on event methods in each model. The strict separation of duties between modules, or "separation of concerns", makes the Algorithm Framework ideal for reusing code between strategies.

## Setting Models

The desired framework models should be set in your **Initialize()** method. Each model is a self contained class which can be imported to your algorithm.

*Universe Models* programmatically select assets to avoid selection bias.

    # Set Universe Model to the NullUniverseSelectionModel class 
    self.SetUniverseSelection(NullUniverseSelectionModel())

**Alpha Models** generate predictions on assets in our universe.

    # Set the Alpha Model to the NullAlphaModel class 
    self.SetAlpha(NullAlphaModel())

**Portfolio Construction Models** optimize the allocatation of resources for best return.

    # Set the Portfolio Construction to the NullPortfolioConstructionModel class
    self.SetPortfolioConstruction(NullPortfolioConstructionModel())

**Risk Models** monitor real-time risk in the portfolio targets.

    # Set the Risk Model to the NullRiskManagementModel class
    self.SetRiskManagement(NullRiskManagementModel())

**Execution Models** efficiently break up orders and fill trades.

    # Set the Execution Model to the NullExecutionModel class
    self.SetExecution(NullExecutionModel())