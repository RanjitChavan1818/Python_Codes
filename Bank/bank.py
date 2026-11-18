# class Bank:
#     Branch_Name="CHAVAN BANK"
#     IFSC_CODE="CHN1234"
#     def __init__(self,cust_id,name,mob_no,email,addr):
#         self.cust_id=cust_id
#         self.name=name
#         self.mob_no=mob_no
#         self.email=email
#         self.addr=addr

from abc import ABC, abstractmethod
from datetime import datetime

class BankException(Exception):
    #Base Exceptions for bank related error
    pass
class InvalidAmountException(BankException):
    pass

class InsufficientBalanceException(BankException):
    pass

class AccountNotFoundException(BankException):
    pass

class CustomerNotFoundException(BankException):
    pass

class AccountBlockedException(BankException):
    pass

class AccountClosedException(BankException):
    pass

class InvalidAccountOperationException(BankException):
    pass


class Transaction:
    transaction_counter = 1000

    def __init__(self,transaction_type, amount, account_number):
        Transaction.transaction_counter += 1

        self.transaction_id =f"T{Transaction.transaction_counter}"
        self.transaction_type = transaction_type
        self.amount = amount
        self.account_number = account_number
        self.timestamp = datetime.now()
        self.balance_after = None

    def __str__(self):
        return (
            f"{self.transaction_id} | "
            f"{self.transaction_type:<15} | "
            f"₹{self.amount:<10} | "
            f"{self.timestamp.strftime('%d-%m-%Y %H:%M:%S')} | "
            f"Balance: ₹{self.balance_after}"
        )

class Customer:
    customer_counter= 100
    def __init__(self,name, mobile, email,address):
        Customer.customer_counter +=1

        self.customer_id=f"C{Customer.customer_counter}"
        self.name=name
        self.mobile=mobile
        self.email=email
        self.address=address

        # One Customer can have multiple accounts
        self.accounts =[]

    def add_account(self,account):
        self.accounts.append(account)

    def show_details(self):
        print("\n -------- Customer Details---------------")
        print("Customer ID :",self.customer_id)
        print("Name        :",self.name)
        print("Mobile      :",self.mobile)
        print("Email       :",self.email)
        print("Address     :",self.address)

        print("\n Accounts:")

        if not self.accounts:
            print("No Accounts.")
        else:
            for account in self.accounts:
                print(
                    account.account_number,
                    "-",
                    account.account_type,
                    "-",
                    account.status

                )


class BankAccount(ABC):
    account_counter=10000

    def __init__(self,customer,initial_deposit=0):
        BankAccount.account_counter+=1

        self.account_number= BankAccount.account_counter
        self.customer=customer

        self.__balance=0
        self.opening_date=datetime.now()
        self.status="ACTIVE"

        self.transactions =[]
        if initial_deposit<0:
            raise InvalidAmountException(
                "Initial Deposit cannot be negative"
            )
        self.__balance=initial_deposit
        if initial_deposit>0:
            transaction =Transaction (
                "DEPOSIT",
                initial_deposit,
                self.account_number
            )

            transaction.balance_after=self.__balance
            self.transactions.append(transaction)


    def _check_active(self):
        if self.status=="CLOSED":
            raise AccountClosedException (
                "Account is closed"
            )
        if self.status == "BLOCKED":
            raise AccountBlockedException(
                "Account is bloacked"
            )

    def deposit(self,amount):
        self._check_active()

        if amount<=0:
            raise InvalidAmountException(
                "Deposit amount must be greater than zero")

        self.__balance+=amount

        transaction = Transaction(
            "DEPOSIT",
            amount,
            self.account_number
        )

        transaction.balance_after=self.__balance
        self.transactions.append(transaction)

    def withdraw(self,amount):
        self._check_active()
        if amount<=0:
            raise InvalidAmountException(
                "Withdrawal amount must be greater than zero"
            )
        self._validate_withdrawal(amount)
        self.__balance -= amount

        transaction =Transaction(
            "WITHDRAW",
            amount,
            self.account_number
        )
        transaction.balance_after =self.__balance
        self.transactions.append(transaction)
    @abstractmethod
    def _validate_withdrawal(self,amount):
        pass
    def get_balance(self):
        self._check_active()
        return self.__balance

    def block(self):
        if self.status=="CLOSED":
            raise AccountClosedException(
                "Closed account cannot be blocked"
            )
        self.status="BLOCKED"

    def unblock(self):
        if self.status=="CLOSED":
            raise AccountClosedException(
                "Closed account cannot be unblocked"
            )
        self.status="ACTIVE"

    def close(self):
        if self.status=="CLOSED":
            raise AccountClosedException(
                "Account is already closed"
            )
        if self.__balance!=0:
            raise InvalidAccountOperationException(
                "Account balance must be zero before closing"
            )
        self.status="CLOSED"





        