"""This module defines the MinimumBalanceStrategy class."""

__author__ = "Edraque Maglaque"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    MinimumBalanceStrategy subclass: Calculates service charges based 
                                     on minimum balance of the account.
    
    """

    def __init__(self, minimum_balance: float):
        """
        Initializes the class attributes with the argument values.

        Args:
            minimum_balance (float): The minimum value a balance can be 
                                     before further service charges 
                                     are applied.
        
        """
        try:
            float(minimum_balance)
            self.__minimum_balance = minimum_balance
        except:
            self.__minimum_balance = 50.00
        
        self.SERVICE_CHARGE_PREMIUM = 2.00
        
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        The strategy to calculate the service charge.

        Args:
            account (BankAccount): The Bank Account type for it's 
                                   service charges to be calculated.

        Returns:
            float: The service charge to be applied.
        
        """
        if account.balance >= self.__minimum_balance:
            service_charge = self.BASE_SERVICE_CHARGE
        else:
            service_charge = self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM

        return service_charge
    