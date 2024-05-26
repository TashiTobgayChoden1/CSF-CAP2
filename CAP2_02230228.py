#name: Tashi Tobgay Choden,
 #section: 1ICE
 #StudentIDNumber: 02230228
 #REFERENCES:
#https://www.codecademy.com/resources/blog/what-is-inheritance/
#https://www.youtube.com/watch?v=irOo4pO-Ros
#https://www.youtube.com/watch?v=ZQkA44lDtIk

# Import necessary modules
import os
import random
import string

# BankAccount class represents a bank account
class BankAccount:
    def __init__(self, account_type, balance=0):
        self.account_number = self.generate_account_number()  # Generate a random account number
        self.password = self.generate_password()  # Generate a random password
        self.account_type = account_type  # Account type (Personal or Business)
        self.balance = balance  # Initial balance

    def generate_account_number(self):
        # Generate a 10-digit random account number
        account_number = ''.join(random.choices(string.digits, k=10))
        return account_number

    def generate_password(self):
        # Generate an 8-character random digits
        password = ''.join(random.choices(string.digits, k=8))
        return password

    def deposit(self, amount):
        self.balance += amount  # Add the amount to the account balance
        print(f"Deposit successful. current acc balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount  # deduct the amount from the account balance
            print(f"Withdrawal successful. current acc balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def transfer(self, recipient_account, amount):
        if self.balance >= amount:
            self.balance -= amount  # deduct the amount from the sender's account
            recipient_account.balance += amount  # Add the amount to the recipient's account
            print(f"Transfer of {amount} successful. Your new balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def __str__(self):
        # Return a string representation of the account
        return f"Account Number: {self.account_number}, Balance: {self.balance}, Account Type: {self.account_type}"

# PersonalAccount class inherits from BankAccount
class PersonalAccount(BankAccount):
    def __init__(self, balance=0):
        super().__init__("Personal", balance)  # Call the parent class constructor

# BusinessAccount class inherits from BankAccount
class BusinessAccount(BankAccount):
    def __init__(self, balance=0):
        super().__init__("Business", balance)  # Call the parent class constructor

def save_account(account):
    # Save account details to a file
    with open("accounts.txt", "a") as file:
        file.write(f"{account.account_number},{account.password},{account.account_type},{account.balance}\n")

def load_accounts():
    accounts = []
    if os.path.exists("accounts.txt"):
        with open("accounts.txt", "r") as file:
            for line in file:
                # Read account details from the file and create account objects
                account_number, password, account_type, balance = line.strip().split(",")
                if account_type == "Personal":
                    account = PersonalAccount(int(balance))
                else:
                    account = BusinessAccount(int(balance))
                account.account_number = account_number
                account.password = password
                accounts.append(account)
    return accounts

def authenticate_account(accounts, account_number, password):
    # Authenticate an account by checking the account number and password
    for account in accounts:
        if account.account_number == account_number and account.password == password:
            return account
    return None

def main():
    accounts = load_accounts()  # Load existing accounts from the file

    while True:
        print("\nWelcome to the Bank!")
        print("1. Create a new account")
        print("2. Log in to an existing account")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            # Create a new account
            print("\nCreate a new account")
            print("1. Personal Account")
            print("2. Business Account")
            account_type = input("Enter account type (1/2): ")

            if account_type == "1":
                account = PersonalAccount()
            elif account_type == "2":
                account = BusinessAccount()
            else:
                print("Invalid choice.")
                continue

            print(f"Account created successfully!\nAccount Number: {account.account_number}\nPassword: {account.password}")
            save_account(account)  # Save the new account to the file

        elif choice == "2":
            # Log in to an existing account
            account_number = input("Enter your account number: ")
            password = input("Enter your password: ")

            account = authenticate_account(accounts, account_number, password)
            if account:
                print(f"\nWelcome, {account.account_type} Account Holder!")
                while True:
                    print("\nWhat would you like to do?")
                    print("1. Check balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transfer funds")
                    print("5. Delete account")
                    print("6. Log out")
                    operation = input("Enter your choice (1/2/3/4/5/6): ")

                    if operation == "1":
                        print(f"Your current balance: {account.balance}")
                    elif operation == "2":
                        amount = int(input("Enter the amount to deposit: "))
                        account.deposit(amount)
                        save_account(account)  # Save the updated account to the file
                    elif operation == "3":
                        amount = int(input("Enter the amount to withdraw: "))
                        account.withdraw(amount)
                        save_account(account)  # Save the updated account to the file
                    elif operation == "4":
                        recipient_account_number = input("Enter the recipient account number: ")
                        recipient_account = authenticate_account(accounts, recipient_account_number, "")
                        if recipient_account:
                            amount = int(input("Enter the amount to transfer: "))
                            account.transfer(recipient_account, amount)
                            save_account(account)  # Save the updated sender's account
                            save_account(recipient_account)  # Save the updated recipient's account
                        else:
                            print("Invalid recipient account number.")
                    elif operation == "5":
                        confirmation = input("Are you sure you want to delete your account? (y/n): ")
                        if confirmation.lower() == "y":
                            accounts.remove(account)
                            print("Account deleted successfully.")
                            save_accounts(accounts)  # Save the updated list of accounts
                            break
                    elif operation == "6":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice.")
            else:
                print("Invalid account number or password.")

        elif choice == "3":
            print("thank you for choosing this bank!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()