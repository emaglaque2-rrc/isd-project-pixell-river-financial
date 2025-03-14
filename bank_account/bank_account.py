"""Description: A class to manage BankAccount objects."""

__author__ = "Edraque Maglaque"
__version__ = "1.2.0"

from abc import ABC, abstractmethod
from datetime import date
from patterns.observer.subject import Subject
from patterns.observer.observer import Observer

class BankAccount(Subject, ABC):
    """BankAccount class: Manages a client's bank account."""

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date):
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

        Raises:
            ValueError: Raised when account_number and client_number is
                        not numeric.

        """

        super().__init__()

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
        except:
            self.__balance = 0

        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()
        
        LARGE_TRANSACTION_THRESHOLD = 9999.99
        LOW_BALANCE_LEVEL = 50.0
        
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

        """
        try:
            valid_amount = float(amount)
            self.__balance += valid_amount
        except:
            pass
        
    def deposit(self, amount: float) -> None:
        """
        Makes a deposit into the client's bank account.

        Args:
            amount (float): The number to be deposited into the bank
                            account's balance.
        
        Raises:
            ValueError: Raised when amount is not numeric and 
                        not positive.
        
        """
        if not isinstance(amount, float):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")
        
        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        """
        Makes a withdrawal from the client's bank account.

        Args:
            amount (float): The number desired to be withdrew from the
                            bank account's balance.
        
        Raises:
            ValueError: Raised when amount is not numeric, not positive,
                        or when the withdrawal amount exceeds the
                        account's balance.
        
        """
        if not isinstance(amount, float):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        
        if amount <= 0:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must be positive.")
        
        if amount > self.__balance:
            raise ValueError(
                f"Withdrawal amount: ${amount:,.2f} must not exceed the "
                + f"account balance: ${self.__balance:,.2f}"
                )
    
        self.update_balance(-amount)

    def __str__(self) -> str:
        """
        Return a string representation of the class instance.

        Returns:
            str: The BankAccount class instance formatted as a string.
        
        """
        return (
            f"Account Number: {self.__account_number} "
            + f"Balance: ${self.__balance:,.2f}\n"
        )
    
    @abstractmethod
    def get_service_charges(self) -> float:
        """
        Return the calculated service charges. 
        Implemented in subclass(es).
        
        """
        pass

    def attach(self, observer: Observer):
        """
        Attaches (adds) an observer to the list of Observers.

        Args:
            observer (Observer): Observer to be added onto the list.
        
        """
        self._observers.append(observer)
    