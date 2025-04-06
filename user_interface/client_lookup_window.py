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
        #self.account_table.cellClicked.connect(self.__on_select_account)

    @Slot()
    def __on_lookup_client(self):
        """
        Retrieves client information based on the client_number_edit
        /textbox widget, then displays the client data such as bank
        accounts on the screen.

        """

        try:
            client_number = int(self.client_number_edit.text())
        except ValueError:
            QMessageBox.information(self, "Input Error",
                                    "The client number must be a numeric value.")
            self.reset_display()
            return
        
        # Check if the client number exists
        if client_number not in self.__client_listing:
            QMessageBox.information(self, "Not Found",
                                    f"Client number: {client_number} not found.")
            self.reset_display()
            return
        
        client = self.__client_listing[client_number]
        self.client_info_label.setText(f"Client Name: {client.first_name} "
                                       + f"{client.last_name}")

        # maybe thing here to reset the tablee? think ahead 

        # COME BACK TO THISSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS

        # counter for the for-loop below
        row = 0

        for account in self.__accounts.values(): 
            if account.client_number == client_number:
                self.account_table.insertRow(row)

                account_number_item = QTableWidgetItem(str(account.account_number))
                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                date_created_item = QTableWidgetItem(str(account._date_created))
                account_type_item = QTableWidgetItem(account.__class__.__name__)

                account_number_item.setTextAlignment(Qt.AlignCenter)
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                date_created_item.setTextAlignment(Qt.AlignCenter)
                account_type_item.setTextAlignment(Qt.AlignCenter)

                self.account_table.setItem(row, 0, account_number_item)
                self.account_table.setItem(row, 1, balance_item)
                self.account_table.setItem(row, 2, date_created_item)
                self.account_table.setItem(row, 3, account_type_item)

                row += 1
        
        self.account_table.resizeColumnsToContents()

    @Slot()
    def __on_text_changed(self):
        """Clears account table when the client number text changes."""

        self.account_table.setRowCount(0)
        