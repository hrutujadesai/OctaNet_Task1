class Account:
    def __init__(self, user_id, pin, balance):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Insufficient funds!")

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.deposit(amount)
            self.transaction_history.append(f"Transferred ${amount} to {recipient.user_id}")
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"Balance: ${self.balance}")

    def display_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)

class ATM:
    def __init__(self):
        self.accounts = {}  # Store user accounts

    def create_account(self, user_id, pin):
        if user_id not in self.accounts:
            self.accounts[user_id] = Account(user_id, pin, 0)
            print("Account created successfully.")
        else:
            print("User ID already exists. Try a different ID.")

    def login(self, user_id, pin):
        if user_id in self.accounts and self.accounts[user_id].pin == pin:
            return self.accounts[user_id]
        else:
            print("Invalid user ID or PIN.")
            return None

    def start(self):
        while True:
            print("\nATM INTERFACE")
            print("1. Transactions")
            print("2. History")
            print("3. Quit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.transactions()
            elif choice == '2':
                self.history()
            elif choice == '3':
                print("Thank you for using our ATM.")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")

    def transactions(self):
        user_id = input("Enter your user ID: ")
        pin = input("Enter your PIN: ")

        account = self.login(user_id, pin)
        if account:
            while True:
                print("\nTRANSACTIONS")
                print("1. Withdraw")
                print("2. Deposit")
                print("3. Transfer")
                print("4. Back to Main Menu")
                transaction_choice = input("Enter your choice: ")

                if transaction_choice == '1':
                    amount = float(input("Enter the amount to withdraw: "))
                    account.withdraw(amount)
                elif transaction_choice == '2':
                    amount = float(input("Enter the amount to deposit: "))
                    account.deposit(amount)
                elif transaction_choice == '3':
                    recipient_id = input("Enter the recipient's user ID: ")
                    recipient = self.login(recipient_id, "")
                    if recipient:
                        amount = float(input("Enter the amount to transfer: "))
                        account.transfer(recipient, amount)
                elif transaction_choice == '4':
                    break
                else:
                    print("Invalid choice. Please select 1, 2, 3, or 4.")

    def history(self):
        user_id = input("Enter your user ID: ")
        pin = input("Enter your PIN: ")

        account = self.login(user_id, pin)
        if account:
            print("\nTRANSACTION HISTORY")
            account.display_transaction_history()


if __name__ == "__main__":
    atm = ATM()
    while True:
        print("\nMAIN MENU")
        print("1. Create Account")
        print("2. Login")
        print("3. Quit")
        main_choice = input("Enter your choice: ")

        if main_choice == '1':
            user_id = input("Enter your user ID: ")
            pin = input("Enter your PIN: ")
            atm.create_account(user_id, pin)
        elif main_choice == '2':
            atm.start()
        elif main_choice == '3':
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
