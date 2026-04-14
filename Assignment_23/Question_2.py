# Write a python program to implement a class named BankAccount with the following requirements:
# The class should contain two instance variables:
#       Name(Account holder name)
#       Amount(Account Balance)
# The class should contain one class variable:
#       ROI(Rate Of Interest),initialized to 10.5
# Define a constructor (__init__) that accepts Name and initial Amount
# Implement the following instance methods:
#       Display() - displays account holder name and current balance
#       Deposit() - accepts an amount from the user and adds it to balance
#       Withdraw() - accepts an amount from the user and substracts it from balance
#       (ensures withdraw is allowed only if sufficient balance exists)
#       CalculateInterest() - calculates and returns interest using formula:
#       Interest = (Amount  *  ROI) / 100
# Create multiple objects and demonstrate all methods

class BankAccount():
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print(self.Name, "Current balance is : ",self.Amount)

    def Deposit(self):
        Amount = int(input("Enter amount to deposit : "))
        self.Amount += Amount
        print("Amount after deposit : ",self.Amount)

    def Withdraw(self):
        Amount = int(input("Enter amount to withdraw : "))
        if(Amount <= self.Amount):
            self.Amount -= Amount
            print("Amount after withdrawal : ",self.Amount)
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest is : ", Interest)

obj1 = BankAccount("Amit", 4000000)

obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()

obj2 = BankAccount("Pooja", 7000000)

obj2.Display()
obj2.Deposit()
obj2.Withdraw()
obj2.CalculateInterest()

