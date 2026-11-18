# class BankAccount:

#     def __init__(self, balance):
#         self.balance = balance
 # Jr asa ek class kela ithe koni pan object create karun balance -ve set karu shaktay, he khup bad aahe
 # Acc.balanc=-5000

# The outside world should not directly modify sensitive data.
# Instead, we want:

# Outside code
#      ↓
#   deposit()
#   withdraw()
#      ↓
#   balance

"""Encapsulation means bundling data and the methods that operate on that data together,
   while controlling how the internal state is accessed or modified."""

#Real implementation
class BankAccount:
    def __init__(self,acc_no,name,balance):
        self.acc_no=acc_no
        self.name=name
        self.__balance=balance

    def deposit(self,amount):
        if amount<0:
            print("Enter a correct Amount!")
            return
        self.__balance+=amount
        print(f"{amount} Deposited Successfully.")

    def withdraw(self,amount):
        if amount<0:
            print("Enter a correct Amount!")
            return
        if amount>self.__balance:
            print("Insufficient Balance.")
            return
        self.__balance-=amount
        print(f"{amount} withdraw successfully.")

    def get_balance(self):
        return f"Current Balance is {self.__balance}"


account = BankAccount(101, "Ranjit", 5000)

account.deposit(2000)

print(account.get_balance())

account.__balance = -10000 #doesn't modify the actual private attribute in the normal way.

print(account.get_balance())

# 🔑 Encapsulation = Protect the object's state

