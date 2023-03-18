# Building Our Portfolio
## Adding and Removing Securities
The **OnSecuritiesChanged** event fires whenever we have changes to our universe. It receives a **SecurityChanges** object containing references to the added and removed securities.

    # List of securities entering the universe
    changes.AddedSecurities
    # List of securities leaving the universe
    changed.RemovedSecurities

To build our portfolio we can loop over the securities changed. The **AddedSecurities** and **RemovedSecurities** properties are lists of security objects.

    def OnSecuritiesChanged(self, changes):
        # Liquidate securities 
        for security in changes.RemovedSecurities:
            if security.Invested:
                    self.Liquidate(security.Symbol)
        
        # SetHoldings for each new asset 
        for security in changes.AddedSecurities:
            self.SetHoldings(security.Symbol, 0.1)