# Execution Model
The Execution Model is responsible for fulfilling the Portfolio Targets set by the Portfolio Construction Model. It seeks to find the optimal price and order size to efficiently fill orders.

Execution models are more commonly used for large volume trades. For example, imagine you have 100,000 trades of AAPL shares, the execution model breaks this order up into smaller pieces so it can be optimally filled.

## Data Flow: Execution Models
![Data Flow: Execution Model](https://cdn.quantconnect.com/i/tu/ExecutionModel3.jpg)

The execution model receives an array of **PortfolioTarget** objects from the risk management model. The execution model must optimially fill these targets. The finaly output of the model is filled orders. The model is free to delay or spread out the fulfillment of orders as it sees fit.

## Setting our Execution Model

We set the execution model in our **Initialize()** method.

    def Initialize(self): 
        # Set the ImmediateExecutionModel()
        self.SetExecution(ImmediateExecutionModel())
    
The Immediate Execution Model uses market orders to immediately fill algorithm portfolio targets.