_5_MIN='5Min'
_15_MIN='15Min'
_30_MIN='30Min'
_ONE_HOUR='1H'
_ONE_DAY='1D'
_ONE_WEEK='1W'
_ONE_MONTH='1Mon'
_ONE_YEAR='1Y'


class Asset(object):
    pass

class BasicAsset(asset):

    def getSymbol(self):
        pass

    def getDataSource(self):
        pass

    def getFrequence(self):
        pass
    
    def getClose(self, from=None, to=None, freq=None):
        pass

    def getOpen(self, from=None, to=None, freq=None):
        pass

    def getHigh(self, from=None, to=None, freq=None):
        pass

    def getLow(self, from=None, to=None, freq=None):
        pass

    def get5Min(self, from=None, to=None, source=None):
        pass

    def get15Min(self, from=None, to=None, source=None):
        pass

    def get30Min(self, from=None, to=None, source=None):
        pass

    def get1Hour(self, from=None, to=None, source=None):
        pass

    def get1Day(self, from=None, to=None, source=None):
        pass

    def get1Week(self, from=None, to=None, source=None):
        pass

    def get1Month(self, from=None, to=None, source=None):
        pass

    def get1Year(self, from=None, to=None, source=None):
        pass

    def validate(self):
        pass

class Stock(BasicAsset):
    pass


class Future(BasicAsset):
    pass


class Option(BasicAsset):
    pass

