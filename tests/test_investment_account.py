"""
Description: Unit tests for the InvestmentAccount subclass.
Usage: To execute all tests in the terminal execute 
       the following command:
                        python -m unittest tests/test_investment_account.py
"""
__author__ = "Edraque Maglaque"
__version__ = "1.0.0"

from bank_account.investment_account import InvestmentAccount
from datetime import date, timedelta
from unittest import TestCase

class TestInvestmentAccount(TestCase):
    """Defines the unit tests for the InvestmentAccount subclass."""

    def setUp(self):
        old_date = date.today() - timedelta(days = 11 * 365.25)
        exact_date = date.today() - timedelta(days = 10 * 365.25)
        young_date = date.today()

        self.old_investment = InvestmentAccount(444, 200304, 0, old_date, 2.00)
        self.exact_investment = InvestmentAccount(444, 200304, 0, exact_date, 2.00)
        self.young_investment = InvestmentAccount(444, 200304, 0, young_date, 2.00)
    
    ### __init__() Tests 

    def test_init_valid_arguments_attributes_set(self):
        investment_account = InvestmentAccount(444, 200304, 0, date.today(), 2.00)

        self.assertEqual(444, investment_account._BankAccount__account_number)
        self.assertEqual(200304, investment_account._BankAccount__client_number)
        self.assertEqual(0, investment_account._BankAccount__balance)
        self.assertEqual(date.today(), investment_account._date_created)
        self.assertEqual(2.00, investment_account._InvestmentAccount__management_fee)

    def test_init_invalid_management_fee_set_to_default_value(self):
        investment_account = InvestmentAccount(444, 200304, 0, date.today(), "invalid")

        self.assertEqual(2.55, investment_account._InvestmentAccount__management_fee)

    ### get_service_charges() Tests

    def test_get_service_charges_date_created_more_than_10_years_charge_equals_base(self):
        expected_service_charge = 0.50
        actual_service_charge = self.old_investment.get_service_charges()

        self.assertEqual(expected_service_charge, actual_service_charge)

    def test_get_service_charges_date_exactly_10_years_charge_equals_base_plus_management(self):
        expected_service_charge = 2.50
        actual_service_charge = self.exact_investment.get_service_charges()

        self.assertEqual(expected_service_charge,actual_service_charge)

    def test_get_service_charges_date_within_10_years_charge_equals_base_plus_management(self):
        expected_service_charge = 2.50
        actual_service_charge = self.young_investment.get_service_charges()

        self.assertEqual(expected_service_charge, actual_service_charge)
