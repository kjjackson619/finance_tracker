import json
import os

class FinanceTracker:
    def __init__(self, data_file="finance_data.json"):
        self.accounts = {}
        self.data_file = data_file
        self.load_data()

    def save_data(self):
        with open(self.data_file, "w") as f:
            json.dump(self.accounts, f)
        print("Data saved successfully.")

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                self.accounts = json.load(f)
            print("Data loaded successfully.")
        else:
            print("No existing data found. Starting fresh.")
    
    def add_account(self, account_name):
        if account_name in self.accounts:
            print(f"Account '{account_name}' already exists.")
        else:
            self.accounts[account_name] = {"balance": 0.0, "transactions": []}
            self.save_data()
            print(f"Account '{account_name}' created successfully.")
    
    def add_transaction(self, account_name, amount, transaction_type, description=""):
        if account_name not in self.accounts:
            print(f"Account '{account_name}' does not exist.")
            return
        else:
            transaction_type = transaction_type.lower()
            
            if transaction_type not in ["income", "expense"]:
                print("Transaction type must be 'income' or 'expense'.")
                return
            
            if transaction_type == "expense":
                amount = -amount 
            
            self.accounts[account_name]["balance"] += amount
            self.accounts[account_name]["transactions"].append({
                "amount": amount,
                "type": transaction_type,
                "description": description
            })
            self.save_data()
            print(f"Transaction added to '{account_name}: {transaction_type} of {amount} for '{description}'.")

    def get_balance(self, account_name):
        if account_name not in self.accounts:
            print(f"Account '{account_name}' does not exist.")
            return None
        else:
            return self.accounts[account_name]["balance"]
        
    def get_all_balances(self):
        total_balance = 0.0
        for account_name, details in self.accounts.items():
            print(f"Balance for account '{account_name}': {details['balance']}")
            total_balance += details["balance"]
        return total_balance
    
    def display_account_summary(self, account_name):
        if account_name not in self.accounts:
            print(f"Account '{account_name}' does not exist.")

        else:
            print(f"Summary for account '{account_name}':")
            print(f"Balance: {self.accounts[account_name]['balance']}")
            for transaction in self.accounts[account_name]['transactions']:
                print(transaction)

    def display_all_summaries(self):
        for account_name in self.accounts:
            self.display_account_summary(account_name)
            print("")

def main():
    tracker = FinanceTracker()

    while True:
        print("\nFinance Tracker Menu")
        print("1. Add Account")
        print("2. Add Transaction")
        print("3. View Account Balance")
        print("4. View All Balances")
        print("5. View Account Summary")
        print("6. View All Summaries")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_name = input("Enter the account name: ")
            tracker.add_account(account_name)
        
        elif choice == "2":
            account_name = input("Enter the account name: ")
            amount = float(input("Enter the amount: "))
            transaction_type = input("Enter the transaction type (income/expense): ").lower()
            description = input("Enter the description: ")
            tracker.add_transaction(account_name, amount, transaction_type, description)

        elif choice == "3":
            account_name = input("Enter the account name: ")
            balance = tracker.get_balance(account_name)
            if balance is not None:
                print(f"Balance for account '{account_name}': {balance}")

        elif choice == "4":
            total_balance = tracker.get_all_balances()
            print(f"Total balance across all accounts: {total_balance}")

        elif choice == "5":
            account_name = input("Enter the account name: ")
            tracker.display_account_summary(account_name)

        elif choice == "6":
            tracker.display_all_summaries()
        
        elif choice == "7":
            print("Exiting Finance Tracker.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

