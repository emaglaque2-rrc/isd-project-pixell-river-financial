# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author

Edraque Maglaque

## Assignment

Assignment 1: Classes, Encapsulation and Unit Test Planning - This
assignment will produce some foundational classes to be used in an
overall system. The classes will incorporate the outcomes associated
with Module 01. Specifically, these classes will incorporate encapsulation
through the use of private attributes and public accessors and mutators.

Assignment 2: Abstraction, Inheritance, and Polymorphism - This
assignment will enable us to apply our knowledge with more foundational concepts
with Object Oriented Programming (OOP) Languages. We will do this by extending
our class diagram and making 3 subclasses of the very first class we made on
assignment 1.

## Encapsulation

Encapsulation was achieved in the BankAccount class by:

1. Making the account_number, client_number, and balance attributes private, which
reinforces data security and integrity by restricting direct/public access.

2. Utilized accessors to provide a way to read the value of private attributes
(account_number, client_number, and balance) without granting direct access to
the attribute itself.

3. Utilized mutators (update_balance, withdraw, and deposit) to control how
values are assigned to private attributes. This reinforces transformation and
validation to the attribute's value. This ensures that the object always remains
in a valid or "consistent" state.
