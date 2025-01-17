# Object-Oriented Programming (OOP)
# In Python almost everything is an object with properties and methods.

# -----Bank Account Example-----
# This example demonstrates the principles of OOP:
# - **Encapsulation:** Combining data (attributes like `full_name`, `acc_number`, etc.)
#   and methods (like `deposit`, `withdraw`) into a single unit (class `Account`).
# - **Objects:** `gilbert_account`, `jackson_account`, etc., are instances of the `Account` class.
# - **Reusability:** The `Account` class acts as a blueprint that can be reused to create multiple account objects.

# A class is a blueprint for creating objects. The `Account` class below represents a bank account.

class Account(object):
    # The __init__() method is the constructor, called automatically when an object is created.
    # It initializes the object's attributes.
    def __init__(self, full_name, acc_number, phone, balance):
        self.full_name = full_name  # Name of the account holder
        self.acc_number = acc_number  # Account number
        self.phone = phone  # Phone number associated with the account
        self.balance = balance  # Account balance

    # Method to deposit money into the account
    def deposit(self, amount):
        # Modify the account's balance by adding the deposit amount
        self.balance += amount
        print(f"Amount {amount} deposited successfully to account {self.acc_number}.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        # Check if the balance is enough for the withdrawal
        if self.balance >= amount:
            self.balance -= amount  # Deduct the withdrawal amount
            print(f"Amount {amount} withdrawn successfully from account {self.acc_number}.")
        else:
            # Notify the user if there are insufficient funds
            print(f"Insufficient funds. Balance is {self.balance}")

    # Method to check the account balance
    def check_balance(self):
        # Display the current account balance
        print(f"Balance for account {self.acc_number} is: {self.balance}")

# Below, we create objects (instances) of the Account class and demonstrate its functionality.

# Creating an account for Gilbert Omosa with initial balance 1250
gilbert_account = Account("Gilbert Omosa", "00001", "0721234567", 1250)

# Creating another account for Curtis Jackson with initial balance 2500
jackson_account = Account("Curtis Jackson", "00002", "0722345678", 2500)

# Creating another account for Michael Chandler with initial balance 5000
michael_account = Account("Michael Chandler", "00003", "0723456789", 5000)

# Creating another account for Jesse Ventura with a different argument order
# Demonstrating the use of keyword arguments to define attributes out of order
jesse_account = Account(balance=5678, acc_number="00004", phone="0724567890", full_name="Jesse Ventura")

# Using the deposit method to add 3750 to Gilbert's account
gilbert_account.deposit(3750)

# Checking the updated balance for Gilbert's account
gilbert_account.check_balance()

# Using the withdraw method to subtract 750 from Curtis Jackson's account
jackson_account.withdraw(750)

# Checking the updated balance for Curtis Jackson's account
jackson_account.check_balance()

# Depositing 25,000 to Michael Chandler's account
michael_account.deposit(25000)

# Withdrawing 5000 from Michael Chandler's account
michael_account.withdraw(5000)

# Checking the updated balance for Michael Chandler's account
michael_account.check_balance()

# Key-Notes:
# 1. **Encapsulation**: All account data (like balance) and operations (like deposit/withdraw) are encapsulated within the Account class.
# 2. **Reusability**: The same `Account` class is reused to create multiple account objects.
# 3. **Constructor Flexibility**: The `__init__()` method allows both positional and keyword arguments for object initialization.
# 4. **Dynamic Behavior**: Methods like `deposit` and `withdraw` dynamically modify object properties, showcasing the power of OOP.
