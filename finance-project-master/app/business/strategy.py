from helper.util import raiseNotDefined


class StrategyAgent(object):
    """
    An agent must define a getAction method
    """
    def getAction(self, state):
        """
        The Agent will receive a market state and must return an action.
        """
        raiseNotDefined()

    def predict(self):
        raiseNotDefined()

class SolonStrategyAgent(StrategyAgent):

    def __init__(self):
        pass

    def getAction(self, state):
        raiseNotDefined()

    def predict(self):
        raiseNotDefined()


class Action(object):
    OPON = "Open"
    CLOSE = "Close"
    NOTHING = "Nothing"
    

    

    
