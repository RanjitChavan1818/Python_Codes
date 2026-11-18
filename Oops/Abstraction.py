# Now imagine our banking application becomes large.

# A customer doesn't care about the internal implementation of withdrawing money.
# They don't need to know:

# Check balance
#       ↓
# Validate amount
#       ↓
# Check transaction limits
#       ↓
# Update balance
#       ↓
# Create transaction record
#       ↓
# Send notification
#       ↓
# Update database

# Using an abstract class
# Suppose every bank account must provide:
# deposit()
# withdraw()
# calculate_interest()

from abc import ABC, abstractmethod
class BankAccount:
    def __init__(self,acc_no,name,balance):
        self.acc_no=acc_no
        self.name=name
        self.__balance=balance

    def deposit(self,amount):
        if amount<0:
            print("Please Enter a vaid Amount !")
            return
        self.__balance+=amount
        print(f"{amount} deposited successfully.")

    def get_balance(self):
        return self.__balance 

    def _withdraw_amount(self,amount):
        """
            Internal Helper Used By Child Class
        """
        self.__balance-=amount
    @abstractmethod
    def withdraw(self,amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass


# Notice:

# @abstractmethod
# def withdraw(self, amount):
#     pass

# We're saying:
# Every type of BankAccount must define how withdrawal works.
# But we're not telling the parent class exactly how.