class ShareModel:
    def __init__(self, date, symbol, ltp, change, high, low, open, qty, turnover):
        self.date = date
        self.symbol = symbol
        self.ltp = ltp
        self.change = change
        self.high = high
        self.low = low
        self.open = open 
        self.qty = qty
        self.turnover = turnover
    
    def toSQL(self):
        return (self.date.isoformat(), self.symbol, self.ltp, self.change, self.high, self.low, self.open, self.qty, self.turnover)