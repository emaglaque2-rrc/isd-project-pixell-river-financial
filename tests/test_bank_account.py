"""
Description: Unit tests for the BankAccount class.
Usage: To execute all tests in the terminal execute 
       the following command:
                        python -m unittest tests/test_bank_account.py
"""
__author__ = "ACE Faculty"
__version__ = "1.1.0"
__credits__ = "Edraque Maglaque"

from bank_account.bank_account import BankAccount
from unittest import TestCase

class TestBankAccount(TestCase):
    """Defines the unit tests for the BankAccount class."""

    def setUp(self):
        self.bank_account = BankAccount(444, 200304, 8.50)
    
    ### __init__() Tests

    def test_init_valid_arguments_attributes_set(self):
        # Arrange & Act
        bank_account = BankAccount(444, 200304, 8.50)

        # Assert
        self.assertEqual(444, bank_account._BankAccount__account_number)
        self.assertEqual(200304, bank_account._BankAccount__client_number)
        self.assertEqual(8.50, round(bank_account._BankAccount__balance, 2))

    def test_init_nonnumeric_balance_set_to_default_value(self):
        # Arrange & Act
        bank_account = BankAccount(444, 200304, "invalid")

        # Assert
        self.assertEqual(0, bank_account._BankAccount__balance)

    def test_init_nonnumeric_account_number_raises_valueerror(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount("invalid", 200304, 8.50)

    def test_init_nonnumeric_client_number_raises_valueerror(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount(444, "invalid", 8.50)
    
    ### account_number Property Tests

    def test_account_number_accessor_valid_account_returns_account_number(self):
        # Arrange
        expected = 444

        # Act & Assert
        self.assertEqual(expected, self.bank_account.account_number)

    ### client_number Property Tests

    def test_client_number_accessor_valid_client_returns_client_number(self):
        # Arrange
        expected = 200304

        # Act & Assert
        self.assertEqual(expected, self.bank_account.client_number)

    ### balance Property Tests

    def test_balance_accessor_valid_balance_returns_balance(self):
        # Arrange
        expected = 8.50

        # Act & Assert
        self.assertEqual(expected, round(self.bank_account.balance, 2))

    ### update_balance() Tests

    def test_update_balance_positive_amount_returns_correct_sum_for_balance(self):
        # Arrange
        expected = 18.50

        # Act
        self.bank_account.update_balance(10.00)

        # Assert
        self.assertEqual(expected, round(self.bank_account._BankAccount__balance, 2))

    def test_update_balance_negative_amount_returns_correct_difference_for_balance(self):
        # Arrange
        expected = 3.50

        # Act
        self.bank_account.update_balance(-5.00)

        # Assert
        self.assertEqual(expected, round(self.bank_account._BankAccount__balance, 2))

    def test_update_balance_nonnumeric_amount_balance_attribute_stays_the_same(self):
        # Arrange
        expected = 8.50

        # Act
        self.bank_account.update_balance("invalid")

        # Assert
        self.assertEqual(expected, round(self.bank_account._BankAccount__balance, 2))

    ### deposit() Tests

    def test_deposit_valid_deposit_amount_returns_correct_balance(self):
        # Arrange
        expected = 18.50

        # Act
        self.bank_account.deposit(10.00)

        # Assert
        self.assertEqual(expected, round(self.bank_account._BankAccount__balance, 2))

    def test_deposit_negative_amount_raises_valueerror(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-10.00)

    ### withdraw() Tests

    def test_withdraw_valid_withdrawal_amount_returns_correct_difference_with_balance(self):
        # Arrange
        expected = 3.50

        # Act
        self.bank_account.withdraw(5.00)

        # Assert
        self.assertEqual(expected, round(self.bank_account._BankAccount__balance, 2))

    def test_withdraw_negative_withdrawal_amount_raises_valueerror(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(-5.00)

    def test_withdraw_withdrawal_amount_exceeds_balance_raises_valueerror(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(10.00)
            
    ### __str__() Tests

    def test_str_valid_bank_account_returns_formatted_string(self):
        # Arrange
        expected = ("Account Number: 444 Balance: $8.50\n")

        # Act & Assert
        self.assertEqual(expected, str(self.bank_account))
