from abc import ABC

from strategy import Strategy


class TestStrategy(Strategy):
    
    def is_buy_condition_met(self):
        pass

    def is_sell_condition_met(self):
        pass

    def __init__(self):
        pass
