import random  # Import the random module for generating random numbers

class BankAccount:
    def __init__(self, account_type):
        self.account_num = self.generate_account_num()  # Generate a random account number
        self.account_type = account_type  # Account type (Personal or Business)
        self.balance = 0  # Initial balance is set to 0

    def generate_account_num(self):
        # Generate a 10-digit random account number
        account_num = ''.join(str(random.randint(0, 9)) for _ in range(10))
        return account_num

    def deposit(self, amount):
        self.balance += amount  # Add the amount to the account balance
        print(f"Deposit successful. Current balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount  # Subtract the amount from the account balance
            print(f"Withdrawal successful. Current balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def transfer(self, recipient, transfer_amount):
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
    def __init__(self):
        super().__init__("Personal")  # Call the parent class constructor with "Personal" as the account type

# BusinessAccount class inherits from BankAccount
class BusinessAccount(BankAccount):
    def __init__(self):
        super().__init__("Business")  # Call the parent class constructor with "Business" as the account type

accounts = []  # List to store all created accounts

def main():
    while True:
        print("\nWelcome to the Bank!")
        print("1. Create a new account")
        print("2. Perform account operations")
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

            print(f"Account created successfully!\nAccount Number: {account.account_num}")
            accounts.append(account)  # Add the new account to the list

        elif choice == "2":
            account_num = input("Enter your account number: ")
            account = next((acc for acc in accounts if acc.account_num == account_num), None)  # Find the account in the list

            if account:
                print(f"\nWelcome, {account.account_type} Account Holder!")
                while True:
                    print("\nWhat would you like to do?")
                    print("1. Check balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transfer funds")
                    print("5. Log out")
                    operation = input("Enter your choice (1/2/3/4/5): ")

                    if operation == "1":
                        print(f"Your current balance: {account.balance}")
                    elif operation == "2":
                        deposit_amount = int(input("Enter the amount to deposit: "))
                        account.deposit(deposit_amount)
                    elif operation == "3":
                        withdrawal_amount = int(input("Enter the amount to withdraw: "))
                        account.withdraw(withdrawal_amount)
                    elif operation == "4":
                        recipient_account_num = input("Enter the recipient account number: ")
                        recipient = next((acc for acc in accounts if acc.account_num == recipient_account_num), None)  # Find the recipient account in the list
                        if recipient:
                            transfer_amount = int(input("Enter the amount to transfer: "))
                            account.transfer(recipient, transfer_amount)
                        else:
                            print("Invalid recipient account number.")
                    elif operation == "5":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice.")
            else:
                print("Invalid account number.")

        elif choice == "3":
            print("Thank you for choosing our bank!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()