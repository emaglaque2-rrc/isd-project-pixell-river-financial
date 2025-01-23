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

        Raises:
            ValueError: Raised when account_number and client_number is
                        not numeric, and when balance can't be converted
                        into a float - then assigns balance a default
                        value of 0.0.

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

    @property
    def account_number(self) -> int:
        """
        The accessor for the account_number attribute. 

        Returns:
            int: An integer value representing the bank account number.
        
        """
        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """
        The accessor for the client_number attribute.

        Returns:
            int: An integer value representing the client number 
                 representing the account holder.
        
        """
        return self.__client_number
    
    @property
    def balance(self) -> float:
        """
        The accessor for the balance attribute.

        Returns:
            float: A float value representing the current balance of 
                   the bank account.
        
        """
        return self.__balance
    
    def update_balance(self, amount: float) -> None:
        """
        Updates the balance of the client's bank account.

        Args:
            amount (float): The number to be added into the bank
                            account, it could be negative as well.
        
        Raises:
            ValueError: Raised when amount is an invalid value.

        """
        try:
            valid_amount = float(amount)
            self.__balance += valid_amount
        except ValueError:
            print("Invalid value, balance not updated.")
        
    def deposit(self, amount: float) -> None:
        """
        Makes a deposit into the client's bank account.

        Args:
            amount (float): The number to be deposited into the bank
                            account.
        
        Raises:
            ValueError: Raised when amount is not numeric and 
                        not positive.
        
        """
        if not isinstance(amount, float):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")
        
        self.update_balance(amount)