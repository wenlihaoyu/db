#from helper.util import raiseNotDefined

class Order(object):
    pass

class MarketOrder(object):
    """
    This is a market order. 
    Attr:
       oid: order id
       timestamp: timestamp for trading
       asset: which asset to trade
       price: price for trading
       num: number for trading
    """
    def __init__(self, oid, timestamp, symbol, price, num):
        self.oid = oid
        self.timestamp = timestamp
        self.symbol = symbol
        self.price = price
        self.num = num

    def getOid(self):
        return self.oid

    def setOid(self, oid):
        self.oid = oid
        
    def getTimestamp(self):
        return self.timestamp

    def setTimestamp(self, timestamp):
        self.timestamp = timestamp

    def getSymbol(self):
        return self.symbol

    def setSymbol(self, symbol):
        self.symbol = symbol

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price
    
    def getNum(self):
        return self.num

    def setNum(self, num):
        self.num = num
        
    def __str__(self):
        return "OrderId: %s\nTimestamp: %s\nSymbol: %s\nPrice: %s\nNum: %s\n" %(self.getOid(), self.getTimestamp(), self.getSymbol(), self.getPrice(), self.getNum())

