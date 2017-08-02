from decimal import *
import time
import uuid


class Account:
    def __init__(self, name, initial_deposit, account_number):
        self.name = name
        self.balance = initial_deposit
        self.account_number = account_number
        print('<Account of {} with initial deposit of {} '
              'has been successfully created. Account No.: {}.>'
              .format(self.name, self.balance, self.account_number))


class Bank:
    accounts = []
    current_account = None

    menu = {
        1: 'New Savings Account',
        2: 'Access an Existing One',
        3: 'Exit'
    }

    def generate_account_number(self):
        return '{0:03d}'.format(len(self.accounts) + 1)

    def deposit(self, account):
        print('Current Balance: {}'.format(account.balance))
        deposit_amount = Decimal(raw_input('Amount to deposit:'))
        account.balance = deposit_amount + Decimal(account.balance)

        print('Successful deposit. Bal: {}'.format(account.balance))
        self.current_account = account
        input()

    def withdraw(self, account):
        print('Current Balance: {}'.format(account.balance))
        withdraw_amount = Decimal(raw_input('Amount to withdraw: '))

        if account.balance >= withdraw_amount:
            account.balance = Decimal(account.balance) - withdraw_amount
            print('Successful withdrawal. Bal: {}'.format(account.balance))
        else:
            print('Insufficient balance.')

        self.current_account = account
        input()

    def view(self, account):
        print('Account No.: {}'.format(account.account_number))
        print('Account Holder: {}'.format(account.name))
        print('Current Balance: {}'.format(account.balance))
        self.current_account = account
        input()

    def access_account(self):
        menu = {
            1: 'Deposit',
            2: 'Withdraw',
            3: 'View',
            4: 'Logout',
        }

        actions =  {
            1: self.deposit,
            2: self.withdraw,
            3: self.view
        }

        print('\nSecurity Questions')
        name = raw_input('What\'s your name? ')
        account_number = raw_input('Account No.? ')

        for index, account in enumerate(self.accounts):
            if account.name == name and account.account_number == account_number:
                current = self.accounts.pop(index)
                break
        else:
            print('\nxxxxxxxxxxxxxxxx')
            print('Login Failed')
            print('xxxxxxxxxxxxxxxx')
            return None

        print('Login Successful')
        while True:
            print('\n-------------------------')
            print('===========MENU==========')
            for key, item in menu.items():
                print('[{}] {}'.format(key, item))

            try:
                choice = input()
                actions[choice](current)
            except Exception as e:
                if choice == 4:
                    self.accounts.append(self.current_account)
                    return

    def add_account(self):
        print('New Savings Account')
        name = raw_input('Name: ')
        initial_deposit = raw_input('Initial deposit (PHP): ')

        account_number = self.generate_account_number()
        depositor = Account(name, initial_deposit, account_number)
        self.accounts.append(depositor)

    def show_menu(self):
        actions = {
            1: self.add_account,
            2: self.access_account,
            3: quit,
        }

        print('\n-------------------------')
        print('===========MENU==========')
        for key, item in self.menu.items():
            print('[{}] {}'.format(key, item))

        try:
            choice = input()
            actions[choice]()
        except Exception as e:
            print(str(e))
            # Disregard the wrong inputs, re-show the menu.
            pass

atm = Bank()
while True:
    atm.show_menu()
