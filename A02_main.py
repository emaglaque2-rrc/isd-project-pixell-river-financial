"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Edraque Maglaque"

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import *
from datetime import date, timedelta

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
try:
    chequing_account = ChequingAccount(444, 200304, -200, date.today(), -100, 0.05)
except ValueError as e:
    print(e)

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(chequing_account)
chequing_account_service_charges = chequing_account.get_service_charges()
print(f"Chequing Account Service Charges: ${chequing_account_service_charges:,.2f}")

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
try:
    chequing_account.deposit(300.00)
except ValueError as e:
    print(e)
print(chequing_account)
chequing_account_service_charges = chequing_account.get_service_charges()
print(f"Chequing Account Service Charges: ${chequing_account_service_charges:,.2f}")

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
try:
    savings_account = SavingsAccount(444, 200304, 55, date.today(), 50.00)
except ValueError as e:
    print(e)

# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(savings_account)
savings_account_service_charges = savings_account.get_service_charges()
print(f"Savings Account Service Charges: ${savings_account_service_charges:,.2f}")

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
try:
    savings_account.withdraw(5.01)
except ValueError as e:
    print(e)
print(savings_account)
savings_account_service_charges = savings_account.get_service_charges()
print(f"Savings Account Service Charges: ${savings_account_service_charges:,.2f}")


print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
try:
    investment_account = InvestmentAccount(444, 200304, 100, date.today(), 2.00)
except ValueError as e:
    print(e)

# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(investment_account)
investment_account_service_charges = investment_account.get_service_charges()
print(f"Investment Account Service Charges: ${investment_account_service_charges:,.2f}")

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
try:
    old_date = date.today() - timedelta(days = 11 * 365.25)
    old_investment_account = InvestmentAccount(444, 200304, 100, old_date, 2.00)
except ValueError as e:
    print(e)

# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(old_investment_account)
old_investment_account_service_charges = old_investment_account.get_service_charges()
print(f"Old Investment Account Service Charges: ${old_investment_account_service_charges:,.2f}")

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
try:
    chequing_account.withdraw(chequing_account_service_charges)
except ValueError as e:
    print(e)

try:
    savings_account.withdraw(savings_account_service_charges)
except ValueError as e:
    print(e)

try:
    investment_account.withdraw(investment_account_service_charges)
except ValueError as e:
    print(e)

try:
    old_investment_account.withdraw(old_investment_account_service_charges)
except ValueError as e:
    print(e)

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print(
    chequing_account,
    savings_account,
    investment_account,
    old_investment_account, sep="\n") 
