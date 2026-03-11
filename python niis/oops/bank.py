class BankAccount:
    
    # Constructor
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
    
    # Deposit Method
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount Deposited:", amount)
    
    # Withdraw Method
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")
    
    # Display Balance
    def check_balance(self):
        print("Current Balance:", self.balance)


# Creating Object
acc1 = BankAccount("Rahul", 12345, 10000)

acc1.deposit(2000)
acc1.withdraw(5000)
acc1.check_balance()