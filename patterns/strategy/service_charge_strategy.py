"""This module defines the ServiceChargeStrategy class."""

__author__ = "Edraque Maglaque"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    ServiceChargeStrategy class: Defines structure for different service 
    charge strategies. Interface to be applied by subclasses.
    
    """

    BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Abstract calculate_service_charges method to be 
        implemented in subclass(es).

        Args:
            account (BankAccount): The Bank Account type for it's 
                                   service charges to be calculated.

        Returns:
            float: The calculated service charge for the corresponding
                   strategy and account. 

        """

        pass 
