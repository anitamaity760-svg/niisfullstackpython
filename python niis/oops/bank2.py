class BankAccount:
    
    # Constructor
    def __init__(self, name, acc_no, balance, rate):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
        self.rate = rate   # Interest Rate (in %)
    
    # Deposit Method
    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
    
    # Withdraw Method
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")
    
    # Interest Calculation (Simple Interest for 1 year)
    def calculate_interest(self):
        interest = (self.balance * self.rate) / 100
        self.balance += interest
        print("Interest Added:", interest)
    
    # Check Balance
    def check_balance(self):
        print("Current Balance:", self.balance)


# Creating Object
acc1 = BankAccount("Rahul", 12345, 10000, 5)

acc1.deposit(2000)
acc1.calculate_interest()
acc1.check_balance()