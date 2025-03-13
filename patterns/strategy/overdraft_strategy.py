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

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        The strategy to calculate the service charge.

        Args:
            account (BankAccount): The Bank Account type for it's 
                                   service charges to be calculated.

        Returns:
            float: The service charge to be applied.
        
        """
        service_charge = 0 
        
        if account.balance >= self.__overdraft_limit:
            service_charge = self.BASE_SERVICE_CHARGE
        else:
            service_charge = (
                self.BASE_SERVICE_CHARGE  
                + (self.__overdraft_limit - account.balance) * self.__overdraft_rate
            )

        return service_charge
    