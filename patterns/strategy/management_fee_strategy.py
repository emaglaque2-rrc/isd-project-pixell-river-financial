"""This module defines the ManagementFeeStrategy class."""

__author__ = "Edraque Maglaque"
__version__ = "1.0.0"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    ManagementFeeStrategy subclass: Calculates service charges based on
                                    the account's date created. 

    """

    def __init__(self, date_created: date, management_fee: float):
        """
        Initializes the class attributes with the argument values.

        Args:
            date_created (date): A date instance representing the date
                                 the account was created.
            management_fee (float): A float which stores a flat-rate 
                                    fee the bank charges for managing 
                                    an account of a certain type.

        """

        if isinstance(date_created, date):
            self.__date_created = date_created
        else:
            self.__date_created = date.today()

        try:
            float(management_fee)
            self.__management_fee = management_fee
        except:
            self.__management_fee = 2.55

        TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

        