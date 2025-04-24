"""The module defines the ClientLookupWindow class."""

__author__ = "ACE Faculty"
__version__ = "3.0.0"
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
        self.filter_button.clicked.connect(self.__on_filter_clicked)

    @Slot()
    def __on_lookup_client(self) -> None:
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
    def __on_text_changed(self) -> None:
        """Clears account table when the client number text changes."""

        self.account_table.setRowCount(0)

    @Slot(int, int)
    def __on_select_account(self, row: int, column: int) -> None:
        """
        Opens the account details window when a bank account is 
        selected.

        Args:
            row (int): Row that has been clicked on.
            column (int): Column that has been clicked on.

        """

        account_number_item = self.account_table.item(row, 0).text()

        # Checks if account_number is not null/blank
        if account_number_item:
            # If the previous validation passed, this will now proceed
            # to the next validation, if not then it will hit the bottom
            # `else`. Also converting it to an int as that's what's
            # it's stored as in self__accounts.
            account_number = int(account_number_item)
            if account_number in self.__accounts:
                bank_account = self.__accounts[account_number]
                account_details = AccountDetailsWindow(bank_account)
                account_details.balance_updated.connect(self.__update_data)
                account_details.exec()
            else:
                QMessageBox.information(self, "No Bank Account",
                                        "Bank Account selected does not exist.")
        else:
            QMessageBox.information(self, "Invalid Selection",
                                    "Please select a valid record.")

    @Slot(BankAccount)
    def __update_data(self, account: BankAccount) -> None:
        """
        Updates the account table with the new account balance.

        Args:
            account (BankAccount): The updated BankAccount object.
        
        """

        for row in range(self.account_table.rowCount()):
            account_number_item = self.account_table.item(row, 0)
            if int(account_number_item.text()) == account.account_number:
                self.account_table.item(row, 1).setText(f"${account.balance:,.2f}")

        self.__accounts[account.account_number] = account

        update_data(account)

    @Slot()
    def __on_filter_clicked(self) -> None:
        """
        Filters or resets the account table based on the current state
        of the filter button and user input.

        ********UNFINISHED ********C HECECK
        """

        if self.filter_button.text() == "Apply Filter":
            filter_combo_box_value = self.filter_combo_box.currentIndex()
            filter_edit_text_value = self.filter_edit.text()

            for row in range(self.account_table.rowCount()):
                record = self.account_table.item(row, filter_combo_box_value)

                if filter_edit_text_value in record.text():
                    self.account_table.setRowHidden(row, False)
                else:
                    # This row does not meet the criteria so it's hidden
                    self.account_table.setRowHidden(row, True)