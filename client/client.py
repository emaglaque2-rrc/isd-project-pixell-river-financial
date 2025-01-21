"""
Description: 
"""

__author__ = "Edraque Maglaque"
__version__ = "1.0.0"

from email_validator import validate_email, EmailNotValidError

class Client:
    """ """

    def __init__(self, client_number: int, first_name: str, last_name: str,
                 email_address: str):
        """
        Initializes the class attributes with the argument values.

        Args:
            client_number (int): An integer value representing the 
                                client number.
            first_name (str): A string value of the client's first name.
            last_name (str): A string value of the client's last name.
            email_address (str): A string value the client's email 
                                address.

        """
