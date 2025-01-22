"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Credits: Edraque Maglaque
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

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

    def test_init_invalid_email_address_raises_emailnotvaliderror_set_to_default_value(self):
        # Arrange & Act
        client = Client(444, "Edraque", "Maglaque", "emaglaque2academicrrcca")

        # Assert
        self.assertEqual("email@pixell-river.com", client._Client__email_address)

