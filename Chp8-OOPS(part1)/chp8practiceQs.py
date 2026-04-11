class Account:
    def __init__(self,balance,account_no):
        self.balance = balance
        self.account_no = account_no

    def credit(self,amount):
        self.balance = self.balance + amount
        print(f"{amount} credited successfully")

    def debit(self,withdraw_amt):
        if withdraw_amt <= self.balance:
            self.balance = self.balance - withdraw_amt
            print(f"{withdraw_amt} debited successfully")
        else:
            print("Insuffient balance")

    def print_balance(self):
        print("Current blance:", self.balance)

amount = Account(0,1234567890)

amt = int(input("Enter a amount to credit:"))
amount.credit(amt)

withdraw = int(input("Enter a amount to withdraw:"))
amount.debit(withdraw)

amount.print_balance()