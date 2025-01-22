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

        Returns:
            ValueError: Raised when client_number is not numeric, and
                        when first_name and last_name is blank.
            EmailNotValidError: Raised when email address is not valid,
                                and then assigns a default email. 
        """

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client Number must be numeric.")
        
        if len(first_name.strip()) > 0:
            self.__first_name = first_name
        else: 
            raise ValueError("First Name cannot be blank.")
        
        if len(last_name.strip()) > 0:
            self.__last_name = last_name
        else:
            raise ValueError("Last Name cannot be blank.")
        
        try:
            validated_email = validate_email(email_address, check_deliverability = False)
            self.__email_address = validated_email.normalized
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"
