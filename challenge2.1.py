class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance is ${self.__account_balance}"
        else:
            return "Deposit amount must be greater than 0."

    def withdraw(self, amount):
        if amount > 0:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                return f"Withdrew ${amount}. New balance is ${self.__account_balance}"
            else:
                return "Insufficient funds for withdrawal."
        else:
            return "Withdrawal amount must be greater than 0."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name}: ${self.__account_balance}"


# Test the BankAccount class
if __name__ == "__main__":
    account = BankAccount("123456789", "John Doe", 1000.0)

    print(account.display_balance())
    print(account.deposit(500.0))
    print(account.withdraw(200.0))
    print(account.display_balance())