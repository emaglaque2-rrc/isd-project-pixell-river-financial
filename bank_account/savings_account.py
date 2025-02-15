"""This module defines the SavingsAccount subclass."""

__author__ = "Edraque Maglaque"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date

class SavingsAccount(BankAccount):
    """SavingsAccount subclass: Clients with savings accounts."""

    def __init__(self, account_number: int, client_number: int, balance: float,
             date_created: date, minimum_balance: float):
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
            minimum_balance (float): The minimum value a balance can be 
                                     before further service charges 
                                     are applied.

        Raises:
            ValueError: Raised when account_number and client_number is
                        not numeric.
        
        """
        super().__init__(account_number, client_number, balance, date_created)

        try:
            float(minimum_balance)
            self.__minimum_balance = minimum_balance
        except:
            self.__minimum_balance = 50.00

        self.SERVICE_CHARGE_PREMIUM = 2.00