__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Edraque Maglaque"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    Represents a window that provides the UI to allow users
    to retrieve Client information and display account details.

    """

    def __init__(self):
        """Initializes a new instance of the ClientLookupWindow"""

        super().__init__()
        client_listing, accounts = load_data()

        self.__client_listing = client_listing
        self.__accounts = accounts

        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)
