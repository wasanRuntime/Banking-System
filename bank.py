class Bank:
    def __init__(self, name):
        self._name = name
        self._balance = 0
    def deposit(self, val):
        if isinstance(val, (float, int)):
            if val > 0:
                self._balance += val
    def withdraw(self, val):
        if isinstance(val, (float, int)):
            if val > 0:
                if self._balance >= val:
                    self._balance -= val
                else: 
                    raise ValueError("You have Insufficient Balance")
            else:
                raise ValueError("Withdrawal amount must be positive")
        else:
            raise ValueError("Withdrawal amount must be a number")
    def __repr__(self):
        return f"Account holder name: {self._name} \nBalance: {self._balance}"

    def get_balance(self):
        return self._balance
# Example usage
account = Bank("Alice")
account.deposit(1000)  # Deposit 1000
print(account.get_balance())  # Output: 1000

account.withdraw(500)  # Withdraw 500
print(account.get_balance())  # Output: 500
print(account)




