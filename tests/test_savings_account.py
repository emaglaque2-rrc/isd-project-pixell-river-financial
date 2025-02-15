"""
Description: Unit tests for the SavingsAccount subclass.
Usage: To execute all tests in the terminal execute 
       the following command:
                        python -m unittest tests/test_savings_account.py
"""
__author__ = "Edraque Maglaque"
__version__ = "1.0.0"

from bank_account.savings_account import SavingsAccount
from datetime import date
from unittest import TestCase

class TestSavingsAccount(TestCase):
    """Defines the unit tests for the SavingsAccount subclass."""

    def setUp(self):
        self.savings_account = SavingsAccount(444, 200304, 55, date.today(), 50.00)

    ### __init__() Tests

    def test_init_valid_arguments_attributes_set(self):
        savings_account = SavingsAccount(444, 200304, 55, date.today(), 50.00)

        self.assertEqual(444, savings_account._BankAccount__account_number)
        self.assertEqual(200304, savings_account._BankAccount__client_number)
        self.assertEqual(55, savings_account._BankAccount__balance)
        self.assertEqual(date.today(), savings_account._date_created)
        self.assertEqual(50.00, savings_account._SavingsAccount__minimum_balance)

    def test_init_invalid_minimum_balance_set_to_default_value(self):
        savings_account = SavingsAccount(444, 200304, 55, date.today(), "invalid")

        self.assertEqual(50.00, savings_account._SavingsAccount__minimum_balance)

    ### get_service_charges() Tests

    def test_get_service_charges_balance_greater_than_minimum_balance_charge_set_to_base_fee(self):
        expected_service_charge = 0.50
        actual_service_charge = self.savings_account.get_service_charges()

        self.assertEqual(expected_service_charge, actual_service_charge)

    def test_get_service_charges_balance_equal_to_minimum_balance_charge_set_to_base_fee(self):
        self.savings_account._BankAccount__balance = 50
        expected_service_charge = 0.50
        actual_service_charge = self.savings_account.get_service_charges()

        self.assertEqual(expected_service_charge, actual_service_charge)

    def test_get_service_charges_balance_less_than_minimum_balance_charge_calculated_accordingly(self):
        self.savings_account._BankAccount__balance = 49.99
        expected_service_charge = 1.00
        actual_service_charge = self.savings_account.get_service_charges()

        self.assertEqual(expected_service_charge, actual_service_charge)

    ### __str__() Tests

    def test_str_valid_savingsaccount_returns_formatted_string(self):
        expected = (
            f"Account Number: 444 Balance: $55.00\n"
            + f"Minimum Balance: $50.00 Account Type: Savings"
        )

        self.assertEqual(expected, str(self.savings_account))
        