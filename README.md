# Bank Account Management System

## Overview

This is a simple Python project that simulates a bank account system. The project includes user account details and basic banking functionalities such as deposits, withdrawals, and balance inquiries.

## Features

* Stores user details (Name, Age, Gender)

* Allows users to view their personal details

* Stores account balance

* Allows deposits

* Allows withdrawals

* Displays the account balance

## Technologies Used

Python 3

## Installation & Usage

### Prerequisites

Ensure you have Python installed on your system.

### Running the Program

1. Clone the repository or copy the script.

2. Open a terminal or command prompt in the project directory.

3. Run the script using the command:

```
python bank_account.py
```

## Class Structure

`User` Class

**Attributes:**

*_name* (str) - User's name

*_age* (int) - User's age

*_gender* (str) - User's gender

**Methods:**

`show_details()` - Displays personal details of the user.

`Bank` Class (Inherits from `User`)

**Additional Attribute:**

`_balance` (float) - Stores account balance, initialized to 0.

**Methods:**

`deposit(amount: float/int)` - Adds money to the balance.

`withdraw(amount: float/int)` - Deducts money from the balance if sufficient funds exist.

`show_balance()` - Displays the account balance.
