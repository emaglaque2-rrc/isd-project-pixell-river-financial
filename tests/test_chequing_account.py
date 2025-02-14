"""
Description: Unit tests for the ChequingAccount subclass.
Usage: To execute all tests in the terminal execute 
       the following command:
                        python -m unittest tests/test_chequing_account.py
"""
__author__ = "Edraque Maglaque"
__version__ = "1.0.0"

from bank_account.chequing_account import ChequingAccount
from datetime import date
from unittest import TestCase

class TestChequingAccount(TestCase):
    """Defines the unit tests for the ChequingAccount subclass."""

    def setUp(self):
        self.chequing_account = ChequingAccount(444, 200304, 0, date(2020, 12, 4),
                                                -100, 0.05)
    