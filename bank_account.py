class Bank_Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        print("Welcome to Jimbo's Bank")

    def get_balance(self):
        return self.balance

    def increase_balance(self,increase):
        return self.balance + increase

    def decrease_balance(self,decrease):
        if decrease < self.balance:
            self.balance -= decrease
            return self.balance
        else:
            print("Sorry, withdrawal amount exceeds balance")


jimbosAccount = Bank_Account("Jimmy",1500)
print(f"${jimbosAccount.get_balance()}")
jimbosAccount.decrease_balance(200)
print(f"${jimbosAccount.get_balance()}")
jimbosAccount.decrease_balance(1301)
print(f"${jimbosAccount.get_balance()}")