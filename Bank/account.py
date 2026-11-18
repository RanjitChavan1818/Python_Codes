class Account:
    def __init__(self,acc_no, holder_name, type,  op_date):
        self.acc_no=acc_no
        self.holder_name=holder_name
        self.type=type
        self.__balance=0
        self.op_date=op_date
        self.acc_status="ACTIVE"

    def deposit(self,amount):
        if amount<=0:
            print("Invalid Amount")

        self.__balance+=amount
        print(f"{amount} successfully deposited.")

    def withdraw(self,amount):
        if amount<=0:
            print("Invalid Amount")

        if amount>self.__balance:
            print("Not Enough sufficient balance available.")

        else:
            print(f"Withdraw {amount}rs successfully.")
            self.__balance -= amount
            print()

    def Check_balance(self):
        print(f"Current Balance is {self.__balance}")

    def account_details(self):
        print(f"Current Balance is:{self.__balance}")

