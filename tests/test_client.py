"""
Description: Unit tests for the Client class.
Usage: To execute all tests in the terminal execute 
       the following command:
                            python -m unittest tests/test_client.py
"""
__author__ = "ACE Faculty"
__version__ = "1.1.0"
__credits__ = "Edraque Maglaque"

from client.client import Client
from unittest import TestCase

class TestClient(TestCase):
    """Defines the unit tests for the Client class."""

    def setUp(self):
        self.client = Client(444, "Edraque", "Maglaque", "emaglaque2@academic.rrc.ca")

    ### __init__() Tests

    def test_init_valid_arguments_attributes_set(self):
        # Arrange & Act
        client = Client(444, "Edraque", "Maglaque", "emaglaque2@academic.rrc.ca")

        # Assert
        self.assertEqual(444, client._Client__client_number)
        self.assertEqual("Edraque", client._Client__first_name)
        self.assertEqual("Maglaque", client._Client__last_name)
        self.assertEqual("emaglaque2@academic.rrc.ca", client._Client__email_address)

    def test_init_invalid_client_number_raises_valueerror(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            client = Client("444", "Edraque", "Maglaque", "emaglaque2@academic.rrc.ca")

    def test_init_blank_first_name_raises_valueerror(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            client = Client(444, "   ", "Maglaque", "emaglaque2@academic.rrc.ca")

    def test_init_blank_last_name_raises_valueerror(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            client = Client(444, "Edraque", "   ", "emaglaque2@academic.rrc.ca")

    def test_init_invalid_email_address_set_to_default_value(self):
        # Arrange & Act
        client = Client(444, "Edraque", "Maglaque", "emaglaque2academicrrcca")

        # Assert
        self.assertEqual("email@pixell-river.com", client._Client__email_address)

    ### client_number Property Tests

    def test_client_number_accessor_valid_client_returns_client_number(self):
        # Arrange
        expected = 444

        # Act & Assert
        self.assertEqual(expected, self.client.client_number)

    ### first_name Property Tests

    def test_first_name_accessor_valid_client_returns_first_name(self):
        # Arrange 
        expected = "Edraque"

        # Act & Assert
        self.assertEqual(expected, self.client.first_name)

    ### last_name Property Tests

    def test_last_name_accessor_valid_client_returns_last_name(self):
        # Arrange
        expected = "Maglaque"

        # Act & Assert
        self.assertEqual(expected, self.client.last_name)

    ### email_address Property Tests

    def test_email_address_accessor_valid_client_returns_email_address(self):
        # Arrange
        expected = "emaglaque2@academic.rrc.ca"

        # Act & Assert
        self.assertEqual(expected, self.client.email_address)

    ### __str__() Tests

    def test_str_valid_client_returns_formatted_string(self):
        # Arrange
        expected = (
            "Maglaque, Edraque [444] - emaglaque2@academic.rrc.ca\n"
        )

        # Act & Assert
        self.assertEqual(expected, str(self.client))
