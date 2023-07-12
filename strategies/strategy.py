"""
This is the base class for strategies, will outline base conditions
that more granular strategies operate on
"""

from abc import abstractmethod


class Strategy:

    @abstractmethod
    def is_buy_condition_met(self):
        pass

    @abstractmethod
    def is_sell_condition_met(self):
        pass
