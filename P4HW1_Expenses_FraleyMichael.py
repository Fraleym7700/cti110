# CTI-110
# P4HW1 - Expenses
# Fraley Michael
# 9/3/2019
keep_going = 'y'

while keep_going == 'y':

#Prompt user to enter amount in account in which money will be withdrawn from.
    Account = float(input('Enter the amount in the account where money will be withdrawn from?  '))

#Prompt the user to enter the title of first expense
    Title_expense  = input('The title of first expense: ')
#Prompt user to enter amount of first expense
    Expense = float(input('The amount of your expense:  '))
#Subtract expense from account
    Ex_amount = Account - Expense
    left_amount = Ex_amount
    print(left_amount)
#Ask user if he/she would like to enter another expense.
    keep_going = input('Do you want to calculate another' + ' expense (Enter y for yes):  ')
# Program DOES NOT move on to next step unless user chooses NOT to enter another expense.
