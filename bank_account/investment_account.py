"""This module defines the InvestmentAccount subclass."""

__author__ = "Edraque Maglaque"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date, timedelta
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    """InvestmentAccount subclass: Clients with investment accounts."""

    def __init__(self, account_number: int, client_number: int, balance: float,
             date_created: date, management_fee: float):
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
            management_fee (float): A float which stores a flat-rate 
                                    fee the bank charges for managing 
                                    an InvestmentAccount.
        
        Raises:
            ValueError: Raised when account_number and client_number is
                        not numeric.
                        
        """
        super().__init__(account_number, client_number, balance, date_created)

        try:
            float(management_fee)
            self.__management_fee = management_fee
        except:
            self.__management_fee = 2.55

        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)
        self.__strategy = ManagementFeeStrategy(date_created, management_fee)

    def __str__(self) -> str:
        """
        Returns a string representation of a InvestmentAccount object.

         Returns:
            str: InvestmentAccount formatted as a string.
        
        """
        
        if self._date_created >= self.TEN_YEARS_AGO:
            management_fee_message = f"${self.__management_fee:,.2f}"
        else:
            management_fee_message = "Waived"

        message = super().__str__()
        message += (
            f"Date Created: {self._date_created} "
            + f"Management Fee: {management_fee_message} Account Type: Investment"
        )

        return message
    
    def get_service_charges(self) -> float:
        """
        Calculates the service charge of the Investment Account.

        Returns:
            float: The service charge of the Investment Account.
        
        """
        return self.__strategy.calculate_service_charges(self)