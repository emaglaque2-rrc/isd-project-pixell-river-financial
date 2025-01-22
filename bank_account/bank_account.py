"""
Description:
"""

__author__ = "Edraque Maglaque"
__version__ = "1.0.0"

class BankAccount:
    """ """

    def __init__(self, account_number: int, client_number: int, balance: float):
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

        """

        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account Number must be numeric.")
        
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client Number must be numeric.")

        try:
            self.__balance = float(balance)
        except ValueError:
            self.__balance = 0.0
