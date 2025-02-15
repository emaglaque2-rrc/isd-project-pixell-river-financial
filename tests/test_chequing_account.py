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
        self.chequing_account = ChequingAccount(444, 200304, 0, date.today(),
                                                -100, 0.05)
    
    ### __init__() Tests

    def test_init_valid_arguments_attributes_set(self):
        chequing_account = ChequingAccount(444, 200304, 0, date.today(), -100, 0.05)

        self.assertEqual(444, chequing_account._BankAccount__account_number)
        self.assertEqual(200304, chequing_account._BankAccount__client_number)
        self.assertEqual(0, chequing_account._BankAccount__balance)
        self.assertEqual(date.today(), chequing_account._date_created)
        self.assertEqual(-100, chequing_account._ChequingAccount__overdraft_limit)
        self.assertEqual(0.05, chequing_account._ChequingAccount__overdraft_rate)

    def test_init_invalid_overdraft_limit_set_to_default_value(self):
        chequing_account = ChequingAccount(444, 200304, 0, date.today(), "invalid", 0.05)

        self.assertEqual(-100, chequing_account._ChequingAccount__overdraft_limit)

    def test_init_invalid_overdraft_rate_set_to_default_value(self):
        chequing_account = ChequingAccount(444, 200304, 0, date.today(), -100, "invalid")

        self.assertEqual(0.05, chequing_account._ChequingAccount__overdraft_rate)

    def test_init_invalid_date_set_to_default_value(self):
        chequing_account = ChequingAccount(444, 200304, 0, "invalid", -100, 0.05)

        self.assertEqual(date.today(), chequing_account._date_created)

    ### get_service_charges() Tests

    def test_get_service_charges_balance_greater_than_overdraft_limit_set_to_base_value(self):
        expected_service_charge = 0.50
        actual_service_charge = self.chequing_account.get_service_charges()

        self.assertEqual(expected_service_charge, actual_service_charge)

    def test_get_service_charges_balance_less_than_overdraft_limit_charges_calculated_accordingly(self):
        self.chequing_account._BankAccount__balance = -600
        expected_service_charge = 25.50
        actual_service_charge = self.chequing_account.get_service_charges()

        self.assertEqual(expected_service_charge, actual_service_charge)

    def test_get_service_charges_balance_equal_to_overdraft_limit_set_to_base_value(self):
        self.chequing_account._BankAccount__balance = -100
        expected_service_charge = 0.50
        actual_service_charge = self.chequing_account.get_service_charges()

        self.assertEqual(expected_service_charge, actual_service_charge)

    ### __str__() Tests

    def test_str_valid_chequingaccount_returns_formatted_string(self):
        expected = (
            "Account Number: 444 Balance: $0.00\n"
            + "Overdraft Limit: $-100.00 Overdraft Rate: 5.00% "
            + "Account Type: Chequing")
        
        self.assertEqual(expected, str(self.chequing_account))
        