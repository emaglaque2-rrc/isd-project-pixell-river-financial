"""
Description: A client program written to verify implementation 
of the Event-Driven Programming Paradigm implemented on top of the 
Object-Oriented Programming Paradigm

"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Edraque Maglaque"

# REQUIREMENT - add import statements
from user_interface.client_lookup_window import ClientLookupWindow

# GIVEN:
from PySide6.QtWidgets import QApplication

# GIVEN:
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = ClientLookupWindow()
    mainWindow.show()
    sys.exit(app.exec())
    