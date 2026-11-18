from Abstraction import BankAccount

class SavingAccount(BankAccount):

    def withdraw(self, amount):
        if amount<0:
            print("Enter a Valid Amount!")
            return
        if amount>self.get_balance():
            print("Insufficient Balance")
            return
        self._withdraw_amount(amount)
        print(f"{amount} withdraw Successfully")

    def calculate_interest(self):
        interest=self.get_balance()*0.04
        return interest

class CurrentAccount(BankAccount):

    def withdraw(self, amount):

        overdraft_limit = 10000

        if amount <= 0:
            print("Invalid amount.")
            return

        if amount > self.get_balance() + overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
            return

        self._withdraw_amount(amount)
        print(f"₹{amount} withdrawn from Current Account.")

    def calculate_interest(self):
        return 0





#POLYMORPHISM
savings = SavingAccount(
    101,
    "Ranjit",
    10000
)

current = CurrentAccount(
    102,
    "Amit",
    10000
)
accounts = [savings, current]
for account in accounts:
    account.withdraw(12000)