__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Edraque Maglaque"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy
from PySide6.QtCore import Qt, Slot

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """

    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()

        if isinstance(account, BankAccount):
            self.__account = copy.deepcopy(account)

            self.account_number_label.setText(str(self.__account.account_number))
            self.balance_label.setText(f"${self.__account.balance:,.2f}")

            self.deposit_button.clicked.connect(self.__on_apply_transaction)
            self.withdraw_button.clicked.connect(self.__on_apply_transaction)
            self.exit_button.clicked.connect(self.__on_exit)
        else:
            self.reject()
    
    @Slot()
    def __on_apply_transaction(self):
        """
        Performs a deposit or withdrawal transaction based on which 
        button was clicked, and updates the balance label accordingly.

        Raises:
            ValueError: Raised when transaction_amount is not numeric, 
                        not positive, or when the withdrawal amount 
                        exceeds the account's balance.
        
        """

        try:
            transaction_amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.information(self, "Invalid Data",
                                    "Amount must be numeric")
            self.transaction_amount_edit.setFocus()
            return
        
        try:
            if self.sender() == self.deposit_button:
                transaction_type = "Deposit"
                self.__account.deposit(transaction_amount)
            elif self.sender() == self.withdraw_button:
                transaction_type = "Withdraw"
                self.__account.withdraw(transaction_amount)
            
            self.balance_label.setText(f"${self.__account.balance:,.2f}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()
        except Exception as e:
            QMessageBox.information(
                                    self,
                                    f"{transaction_type} Failed",
                                    {str(e)})
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

    def __on_exit(self):
        pass