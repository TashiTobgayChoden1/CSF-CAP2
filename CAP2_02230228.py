import os  # Import the os module for file operations
import random  # Import the random module for generating random numbers

class BankAccount:
    def __init__(self, account_type, initial_balance=0):
        self.account_num = self.generate_account_num()  # Generate a random account number
        self.access_code = self.generate_access_code()  # Generate a random access code
        self.account_type = account_type  # Account type (Personal or Business)
        self.balance = initial_balance  # Initial account balance

    def generate_account_num(self):
        # Generate a 10-digit random account number
        account_num = ''.join(str(random.randint(0, 9)) for _ in range(10))
        return account_num

    def generate_access_code(self):
        # Generate an 8-digit random access code
        access_code = ''.join(str(random.randint(0, 9)) for _ in range(8))
        return access_code

    def deposit_funds(self, amount):
        self.balance += amount  # Add the amount to the account balance
        print(f"Deposit successful. Current balance: {self.balance}")

    def withdraw_funds(self, amount):
        if self.balance >= amount:
            self.balance -= amount  # Subtract the amount from the account balance
            print(f"Withdrawal successful. Current balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def transfer_funds(self, recipient, transfer_amount):
        if self.balance >= transfer_amount:
            self.balance -= transfer_amount  # Subtract the transfer amount from the sender's account
            recipient.balance += transfer_amount  # Add the transfer amount to the recipient's account
            print(f"Transfer of {transfer_amount} successful. Your new balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def __repr__(self):
        # Return a string representation of the account
        return f"Account Number: {self.account_num}, Balance: {self.balance}, Account Type: {self.account_type}"

# PersonalAccount class inherits from BankAccount
class PersonalAccount(BankAccount):
    def __init__(self, initial_balance=0):
        # Call the parent class constructor with "Personal" as the account type
        BankAccount.__init__(self, "Personal", initial_balance)

# BusinessAccount class inherits from BankAccount
class BusinessAccount(BankAccount):
    def __init__(self, initial_balance=0):
        # Call the parent class constructor with "Business" as the account type
        BankAccount.__init__(self, "Business", initial_balance)

def save_account_details(account):
    # Save account details to a file
    with open("accounts.txt", "a") as file:
        file.write(f"{account.account_num},{account.access_code},{account.account_type},{account.balance}\n")

def load_account_details():
    accounts = []
    if os.path.exists("accounts.txt"):
        with open("accounts.txt", "r") as file:
            for line in file:
                # Read account details from the file and create account objects
                account_num, access_code, account_type, balance = line.strip().split(",")
                if account_type == "Personal":
                    account = PersonalAccount(int(balance))
                else:
                    account = BusinessAccount(int(balance))
                account.account_num = account_num
                account.access_code = access_code
                accounts.append(account)
    return accounts

def authenticate(accounts, account_num, access_code):
    # Authenticate an account by checking the account number and access code
    for account in accounts:
        if account.account_num == account_num and account.access_code == access_code:
            return account
    return None

def main():
    accounts = load_account_details()  # Load existing accounts from the file

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
            account_type_choice = input("Enter account type (1/2): ")

            if account_type_choice == "1":
                account = PersonalAccount()
            elif account_type_choice == "2":
                account = BusinessAccount()
            else:
                print("Invalid choice.")
                continue

            print(f"Account created successfully!\nAccount Number: {account.account_num}\nAccess Code: {account.access_code}")
            save_account_details(account)  # Save the new account to the file

        elif choice == "2":
            # Log in to an existing account
            account_num = input("Enter your account number: ")
            access_code = input("Enter your access code: ")

            account = authenticate(accounts, account_num, access_code)
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
                        deposit_amount = int(input("Enter the amount to deposit: "))
                        account.deposit_funds(deposit_amount)
                        save_account_details(account)  # Save the updated account to the file
                    elif operation == "3":
                        withdrawal_amount = int(input("Enter the amount to withdraw: "))
                        account.withdraw_funds(withdrawal_amount)
                        save_account_details(account)  # Save the updated account to the file
                    elif operation == "4":
                        recipient_account_num = input("Enter the recipient account number: ")
                        recipient = authenticate(accounts, recipient_account_num, "")
                        if recipient:
                            transfer_amount = int(input("Enter the amount to transfer: "))
                            account.transfer_funds(recipient, transfer_amount)
                            save_account_details(account)  # Save the updated sender's account
                            save_account_details(recipient)  # Save the updated recipient's account
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
                print("Invalid account number or access code.")

        elif choice == "3":
            print("Thank you for choosing our bank!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()