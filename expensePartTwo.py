# CTI-110
# P4HW1 - Expenses
# Fraley Michael
# 9/3/2019
loop = 'y'
#Prompt user to enter amount in account in which money will be withdrawn from.
#Prompt the user to enter the title of first expense
#Subtract expense from account
#Ask user if he/she would like to enter another expense.
def main():
    Account = float(input('Enter the amount in the account where money will be withdrawn from?  '))
    title_expense = input('The title of first expense: ')
    Expense = float(input('The amount of your expense:  '))
    ex_amount = Account - Expense

def func()
    print('--------------------')
    print()
    loop = input('Do you want to calculate another' + ' expense (Enter y for yes):  ')
# Program DOES NOT move on to next step unless user chooses NOT to enter another expense.
