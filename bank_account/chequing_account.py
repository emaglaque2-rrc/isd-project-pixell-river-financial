"""This module defines the ChequingAccount subclass."""

__author__ = "Edraque Maglaque"
__version__ = "1.2.0"

from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    """ChequingAccount subclass: Clients with chequing accounts."""

    def __init__(self, account_number: int, client_number: int, 
                 balance: float, date_created: date, 
                 overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the class attributes with the argument values.

        Args:
            account_number (int): An integer value representing the bank
                                  account number.
            client_number (int): An integer value representing the 
                                 client number representing the 
                                 account holder.
            balance (float): A float value representing the current 
                             balance of the bank account.
            date_created (date): A date instance representing the date
                                 the account was created.
            overdraft_limit (float): The maximum amount a balance can 
                                     be overdrawn (below 0.00) before 
                                     overdraft fees are applied.
            overdraft_rate (float): The rate to which overdraft fees 
                                    will be applied.

        Raises:
            ValueError: Raised when account_number and client_number is
                        not numeric.
        
        """
        super().__init__(account_number, client_number, balance, date_created)

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

        self.__strategy = OverdraftStrategy(overdraft_limit, overdraft_rate)
            
    def __str__(self) -> str:
        """
         Returns a string representation of a ChequingAccount object.

         Returns:
            str: ChequingAccount formatted as a string.
        
        """
        message = super().__str__()
        message += (
            f"Overdraft Limit: ${self.__overdraft_limit:.2f} "
            + f"Overdraft Rate: {self.__overdraft_rate:.2%} "
            + "Account Type: Chequing"
        )
        return message
    
    def get_service_charges(self) -> float:
        """
        Calculates the service charge of the Chequing Account.

        Returns:
            float: The service charge of the Chequing Account.
        
        """
        return self.__strategy.calculate_service_charges(self)
    