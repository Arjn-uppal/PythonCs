class Account:

    # Constructor
    def __init__(self, owner, balance):

        #Set the owner
        self.owner = owner

        #Check for positive Balance and Set it
        if balance >= 0:
            self.balance = balance
        else:
            print("Invalid Balance: Default to Balance of zero")
            self.balance = 0

    # Behaviour Methods
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
        else:
            print("Error: Positive Deposit Required")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance = self.balance - amount
            else:
                print("Error: you didn't have that much")
        else:
            print("Error: Positive Withdrawal Required")

    def __str__(self):
        return "Owner: " + self.owner + "\nBalance: $" + str(self.balance) + "\n"

def main():

    # Solve a problem
    # Creating new account object using the constructor

    a1 = Account("Ron Weasley", 1000)
    a2 = Account("Harry Potter", 4000)

    # Using the behaviour Methods
    a1.withdraw(300)
    a2.withdraw(500)
    a1.deposit(1000)
    a2.deposit(6000)

    # Displaying the values of some instance variables called owner and balance
    print(a1.owner)
    print(a1.balance)

    #Modify instance variables (change specific attribute)
    a1.balance = 20000
    print()
    print(a1.balance)

    a1.withdraw(300)
    print(a1)


main()