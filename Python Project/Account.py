# 1. Create Account
# 2. Deposit Money
# 3. Withdraw Money
# 4. Check Balance
# 5. Display Account
# 6. Exit
class Account:
    def __init__(self,acc_no,name,balance):
        self.acc_no=acc_no
        self.name=name
        self.balance=balance


    def deposit(self,amount):
        if amount<=0:
            print("You Enter wrong Amount")
        else:
            self.balance+=amount
            print(f"Amount Deposited Successfully, Current Balance is {self.balance}")

    def withdraw(self,amount):
        if amount<=0:
            print("You Enter wrong Amount")
        else:
            if amount>self.balance:
                print("Sorry Not Enough money to withdraw")
            else:
                self.balance-=amount
                print(f"{amount} withdraw successfully. Current Balace is {self.balance}")

    def check_balance(self):
        print(f"Current Balance is {self.balance}")

    def display(self):
        print(f"Name:{self.name}")
        print(f"Acc No:{self.acc_no}")
        print(f"Balance:{self.balance}")


accounts=[]
while True:
    print("1.Create Account")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Check Balance")
    print("5.Display details")
    print("6.Exit")

    ch=int(input("Enter Choice:"))
    match ch:
        case 1:
            acc_no=int(input("Enter Account Number:"))
            name=input("Enter Your Name:")
            balance=float(input("Enter how much you store:"))
            acc=Account(acc_no,name,balance)
            accounts.append(acc)
            print("Your successfully add in XYZ Bank")
            print()

        case 2:
            ac_no=int(input("Enter Account Number:"))
            
            for acc in accounts:
                if acc.acc_no==ac_no:
                    amount=float(input("Enter Amount to be deposit:"))
                    acc.deposit(amount)
                    print()
                    break
            else:
                print("Account not Found")

        case 3:
            ac_no=int(input("Enter Account Number:"))
            
            for acc in accounts:
                if acc.acc_no==ac_no:
                    amount=float(input("Enter Amount to be withdraw:"))
                    acc.withdraw(amount)
                    print()
                    break
            else:
                print("Account Not Exist")

        case 4:
            ac_no=int(input("Enter Account Number:"))
            for acc in accounts:
                if acc.acc_no==ac_no:
                    acc.check_balance()
                    print()
                    break
            else:
                print("Account Not Found")

        case 5:
            ac_no=int(input("Enter Account Number:"))
            print()
            for acc in accounts:
                if acc.acc_no==ac_no:
                    acc.display()
                    print()
                    break
            else:
                    print("Account Not Found")
        case 6:
            print("Closing the application...")
            break

        case _:
            print("Invalid Choice!")



            

