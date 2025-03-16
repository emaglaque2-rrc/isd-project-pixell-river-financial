"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Edraque Maglaque"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account import *
from datetime import date
from client.client import Client




# 2. Create a Client object with data of your choice.
try:
    client_one_laurie = Client(1, "Laurie", "Cutrone", "edraque4@gmail.com")
except ValueError as e:
    print(e)



# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
try:
    chequing_account_client_one = ChequingAccount(10001, client_one_laurie.client_number,
                                                  500.00, date.today(),
                                                  100.00, 0.05)
except ValueError as e:
    print(e)

try:
    savings_account_client_one = SavingsAccount(10002, client_one_laurie.client_number,
                                                1850.00, date.today(), 
                                                1000.00)
except ValueError as e:
    print(e)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
try:
    chequing_account_client_one.attach(client_one_laurie)
except Exception as e:
    print(e)

try:
    savings_account_client_one.attach(client_one_laurie)
except Exception as e:
    print(e)




# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
try:
    client_two_damien = Client(2, "Damien", "Altenburg", "r3bornbox@gmail.com")
except ValueError as e:
    print(e)

try:
    savings_account_client_two = SavingsAccount(10003, client_two_damien.client_number,
                                                2500.00, date.today(),
                                                1500.00)
except ValueError as e:
    print(e)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

# Transactions for Client 1 - Chequing Account 
try:
    chequing_account_client_one.deposit(200.00)
except ValueError as e:
    print(e)

try:
    chequing_account_client_one.withdraw(55.00)
except ValueError as e:
    print(e)

try:
    chequing_account_client_one.withdraw(600.00)
except ValueError as e:
    print(e)

# Transactions for Client 1 - Saving Account 
try:
    savings_account_client_one.deposit(11111.00)
except ValueError as e:
    print(e)

try:
    savings_account_client_one.deposit(10.50)
except ValueError as e:
    print(e)

try:
    savings_account_client_one.withdraw(12950.00)
except ValueError as e:
    print(e)

# Transactions for Client 2 - Saving Account 
try:
    savings_account_client_two.deposit(11000.00)
except ValueError as e:
    print(e)

try:
    savings_account_client_two.withdraw(500.00)
except ValueError as e:
    print(e)

try:
    savings_account_client_two.withdraw(12955.00)
except ValueError as e:
    print(e)
