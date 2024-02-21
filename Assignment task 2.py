class BankAccount:
    def __init__(self, acc_num, balance, acc_holder):
        self.acc_num = acc_num
        self.balance = balance
        self.acc_holder = acc_holder

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance
#creating an instance for bank account   
acc1= BankAccount(acc_num=11223344, balance=1000, acc_holder='Rushmitha')
acc1.deposit(200)  # Deposit ammt of 200
acc1.withdraw(700)  # Withdraw ammt of 700
print(f'The total balance of the account is: {acc1.get_balance()}')










class BankAccount:
    def __init__(self, acc_number, balance, acc_holder):
        self.acc_number = acc_number
        self.balance = balance
        self.acc_holder = acc_holder

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

class CheckingAccount(BankAccount):
    def __init__(self, acc_number, balance, acc_holder, transaction_fees):
        super().__init__(acc_number, balance, acc_holder)
        self.transaction_fees = transaction_fees

    def apply_transaction_fees(self):
        self.balance -= self.transaction_fees

checking_account = CheckingAccount(acc_number=11223344, balance=1000, acc_holder='Rushmitha', transaction_fees=30.50)


checking_account.apply_transaction_fees()

print(f' after applying transaction fees The total balance is: {checking_account.get_balance()}')










class BankAccount:
    def __init__(self, acc_num, balance, acc_holder):
        self.acc_num = acc_num
        self.balance = balance
        self.acc_holder = acc_holder

    def deposit(self, ammt):
        self.balance += ammt

    def withdraw(self, ammt):
        if self.balance >= ammt:
            self.balance -= ammt
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, acc_num, balance, acc_holder, intrst_rate):
        super().__init__(acc_num, balance, acc_holder)
        self.intrst_rate = intrst_rate

    def calculate_interest(self):
        intrst_amount = self.balance * self.intrst_rate
        self.balance += intrst_amount


savings_account = SavingsAccount(acc_num=11223344, balance=1000, acc_holder='Rushmitha', intrst_rate=0.10)


savings_account.calculate_interest()

print(f'The total balance of  account after adding interest is: {savings_account.get_balance()}')





