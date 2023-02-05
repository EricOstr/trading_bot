class CPPLimitOrder():

    def __init__(self, clientOrderID="", tradingPair="", isBuy=False, baseCurrency="", quoteCurrency="", price=None, quantity=None, filledQuantity=None, creationTimestamp=0.0, status=0):
        self.clientOrderID = clientOrderID
        self.tradingPair = tradingPair
        self.isBuy = isBuy
        self.baseCurrency = baseCurrency
        self.quoteCurrency = quoteCurrency
        self.price = price
        self.quantity = quantity
        self.filledQuantity = filledQuantity
        self.creationTimestamp = creationTimestamp
        self.status = status


    def getClientOrderID(self):
        return self.getClientOrderID

    def getTradingPair(self):
        return self.getTradingPair  

    def getIsBuy(self):
        return self.isBuy

    def getBaseCurrency(self):
        return self.getBaseCurrency

    def getQuoteCurrency(self):
        return self.quoteCurrency

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.getQuantity

    def getFilledQuantity(self):
        return self.getFilledQuantity

    def getCreationTimestamp(self):
        return self.getCreationTimestamp

    def getStatus(self):
        return self.status