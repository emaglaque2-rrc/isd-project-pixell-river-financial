"""This module defines the OverdraftStrategy class."""

__author__ = "Edraque Maglaque"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """
    OverdraftStrategy subclass: Calculates service charges based on 
                                overdraft usage.
    
    """

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the class attributes with the argument values.

        Args: 
            overdraft_limit (float): The maximum amount a balance can 
                                     be overdrawn (below 0.00) before 
                                     overdraft fees are applied.
            overdraft_rate (float): The rate to which overdraft fees 
                                    will be applied.
        
        """

        try:
            float(overdraft_limit)
            self.__overdraft_limit = overdraft_limit
        except:
            self.__overdraft_limit = -100

        try:
            float(overdraft_rate)
            self.__overdraft_rate = overdraft_rate
        except:
            self.__overdraft_rate = 0.05

