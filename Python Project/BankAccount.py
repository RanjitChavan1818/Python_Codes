class BankAccount:
    Branch="Javale"
    IFSC_Code="CHAVAN12390"
    
    def __init__(self,holder_name,acc_no):
        self.holder_name=holder_name
        self.acc_no=acc_no
        self.__balance=0

    def deposit(self,amount):
        if amount<0:
            print("Enter amount is invalid.")
            print()
        else:
            self.__balance+=amount
            print(f"Amount {amount} deposited successfully.")
            print()


    def withdraw(self,amount):
        if amount<=0:
            print("Invalid Amount")
            return
        if amount>self.__balance:
            print("Not Sufficient Balance")
            print()
            return
        
            
        print("Withdraw Successfully")
        print("Current Balance is:",self.__balance-amount)
        self.__balance-=amount
        print()

    def check_balance(self):
        print("Current Balance is:",self.__balance)
        print()


R=BankAccount("Ranjit Netaji Chavan",123456789)
# R.deposit(10000)
# R.check_balance()
print("<--------****[ WELCOME TO CHAVAN BANK]****--------->")
while True:
    print("1.Deposit\n2.Withdraw\n3.Check Balance\n4.Exit")
    n=int(input("Enter choice for above options:"))
    match n:
        case 1: 
            amount=int(input("Enter amount for deposit: "))
            R.deposit(amount)
        case 2: 
            amount=int(input("Enter amount for withdraw: "))
            R.withdraw(amount)
        case 3:
            R.check_balance()
        case _:
            print("Exiting......")
            break
    if n==4:
        break