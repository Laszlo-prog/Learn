class BankAccount:
    #Initialize bank account wit zero balance
    def __init__(self, name, pin, balance= 0):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.history = [ ]

#Deposite money into account
    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited: ${amount}")
        print(f"${amount} deposited! New balance: ${self.balance}")
#Withdraw money from account
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdraw ${amount}")
            print(f"${amount} withdrawn! New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

#Show balance:
    def show_balance(self):
        print(f"Account Holder: {self.name}, Current balance: ${self.balance}")
#Show transaction history
    def show_history(self):
        print("\n Transaction Histroy: ")
        for t in self.history:
            print(t) if self.history else print("No transactions yet.")
# ====Main Program=====
name = input("Enter account holder name: ")
pin = input("Set a 4-digit PIN: ")
account = BankAccount(name, pin)
#Ask for pin before 
if input("Enter PIN to login: ") != account.pin:
    print("Incorrect PIN. Exiting.")
    exit()
while True:
    print("\nBank Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Show Transaction History")
    print("5. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
       account.deposit(int(input("Enter amount:")))
    elif choice == '2':
        account.withdraw(int(input("Enter amount:")))
    elif choice == '3':
        account.show_balance()
    elif choice == '4':
        account.show_history()
    elif choice == '5':
        print("Exiting. Thank you for banking with us!")
        break

    else:
        print("Invalid choice. Please try again.")
