from colorama import Fore


class Account:
    def __init__(self, account_type, account_bal):
        self.account_type = account_type
        self.account_bal = account_bal

    def deposit(self, amount):
        self.account_bal += amount

    def withdraw(self, amount):
        # check that the amount to be withdrawn is not greater that the available balance
        if amount < self.account_bal:
            self.account_bal -= amount
        else:
            print(
                Fore.RED + "<ERROR-MESSAGE> Unable to complete this request. You have insufficient funds" + Fore.RESET)


class SavingsAccount(Account):
    def __init__(self, account_bal):
        super().__init__("Savings Account", account_bal)
        self.account_bal = account_bal


class CreditCardAccount(Account):
    def __init__(self, account_bal):
        super().__init__("Credit card Account", account_bal)
        self.account_bal = account_bal


if __name__ == '__main__':
    print("Creating a savings account with initial 200 amount")
    savings_account = SavingsAccount(200.0)
    print("Savings account Bal: ", savings_account.account_bal)
    # deposit to savings account
    print(">> depositing 450 to savings account")
    savings_account.deposit(450)
    print("Savings account Bal: ", savings_account.account_bal)
    # withdraw funds
    print(">> withdrawing 250 from saving account")
    savings_account.withdraw(250)
    print("Savings account Bal: ", savings_account.account_bal)
    print(">> withdrawing 750 from saving account")
    savings_account.withdraw(750)
    print("Savings account Bal: ", savings_account.account_bal)
    print(">> withdrawing 300 from saving account")
    savings_account.withdraw(300)
    print("Savings account Bal: ", savings_account.account_bal)

    print("\nCreating a credit card account with initial 400 amount")
    credit_card_account = CreditCardAccount(400.0)
    print("Credit account Bal: ", credit_card_account.account_bal)
    print(">> depositing 100 to credit card account")
    credit_card_account.deposit(100)
    print("Credit account Bal: ", credit_card_account.account_bal)
    print(">> charge 150 from credit card account")
    credit_card_account.withdraw(150)
    print("Credit account Bal: ", credit_card_account.account_bal)
    print(">> charge 150 from credit card account")
    credit_card_account.withdraw(100)
    print("Credit account Bal: ", credit_card_account.account_bal)
    print(">> charge 600 from credit card account")
    credit_card_account.withdraw(600)
