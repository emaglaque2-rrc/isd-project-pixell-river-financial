# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author

Edraque Maglaque

## Assignment

**Assignment 1**:

- Classes, Encapsulation and Unit Test Planning - This
assignment will produce some foundational classes to be used in an
overall system. The classes will incorporate the outcomes associated
with Module 01. Specifically, these classes will incorporate encapsulation
through the use of private attributes and public accessors and mutators.

**Assignment 2**:

- Abstraction, Inheritance, and Polymorphism - This
 assignment will enable us to apply our knowledge with more foundational concepts
 with Object Oriented Programming (OOP) Languages. We will do this by extending
 our class diagram and making 3 subclasses of the very first class we made on
 assignment 1.

**Assignment 3**:

- Design Patterns, Strategy, and Observer - This
  assignment will address potential issues associated with the maintainability
  and scalability of the current service charge calculation functionality from
  assignment 2. We will address these issues by applying design patterns,
  specifically strategy and observer patterns onto our classes.

**Assignment 4**:

- PySide6, GUI, and data management - This assignment will incorporate a
  Graphical User Interface (GUI) into the PiXELL-River Financial banking system.
  The end product will include a lookup window from which users can view
  existing Client and corresponding Bank Account data. The user can then select
  a Bank Account and perform deposit and withdraw transactions against the selected
  Bank Account. PySide6 will be used to produce the windows and the design of
  these windows will be given so that students can focus on implementing the
  Event Driven Programming Paradigm into their existing set of classes.

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

## Polymorphism

Polymorphism was achieved in the BankAccount subclasses by:

1. Utilizing method overriding within each subclass of BankAccount where the
   get_service_charges method resides in, so it will do it's implementation
   regardless of which instance or subclass it got invoked in, this ensures a
   flexible usage of it.

2. Within the client program, the get_service_charges method got called multiple
   times, however it produced different results each time based on the object
   that was calling it.

## Strategy Pattern

- In this application, we utilize the strategy pattern to handle various types
  of banking accounts. Each type of bank account has it's own specific strategy
  for calculating service charges, which is encapsulated in the whole ecosystem
  of the Strategy Pattern classes. By implementing a design pattern for
  calculating service charges, we are accounting for the future and scalability.
  That means, in the future, we can EASILY accommodate a lot of different type
  of bank accounts and not duplicate code a lot. Also, this allows us to change
  service charge calculations in one place if we ever need to, not in multiple
  files/classes.
  
## Observer Pattern

- In this application, we utilize the observer pattern to notify clients about
  any unusual activity within their accounts. We do this by emailing them about
  the details of the transaction that transpired. Now, we also implemented a
  "subscription" mechanism where the clients have the option to either receive
  or not receive the notifications/emails. Essentially, the BankAccount class
  which is the Subject maintains a list of subscribed clients and notifies them
  when either their account balance is below a pre-defined minimum threshold OR
  a significant transaction has occurred. By implementing a design pattern for
  notifying clients, this enhances their user experience when they're using our
  services and we can extend this feature further by implementing various types
  of notifications without modifying existing code/logic.
  