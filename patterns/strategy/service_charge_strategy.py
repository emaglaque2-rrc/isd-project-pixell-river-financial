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

    BASE_SERVICE_CHARGE: float = 0.50

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Abstract calculate_service_charges method to be 
        implemented in subclass(es).

        Returns:
            float: TO BE FILEDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD

        """

        pass 
