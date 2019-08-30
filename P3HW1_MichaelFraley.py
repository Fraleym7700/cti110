#Ask for the price of food
original_price = float(input("Enter the item's Original Price:   "))

#ask for the tip to server
try:
    tip = float(input("Enter the Tip amount 16%, 18%, 20%:   "))
except:
    def tip_function (number):
        if not  .16 :
            print("not valid input")
        elif not .18 :
            print("not valid input")
        elif not .20 :
            print("not valid input")


# ask for the tax amount
tax = .06

#Calculate the tip and tax
Tip_amount = original_price * tip

Tax_amount = original_price * tax

Total_cost = original_price + Tax_amount + Tip_amount

Tax_tip = Tax_amount + Tip_amount

#When an accurate percentage is entered ,
# the program is then going to calculate the tip and and 6 percent sales tax .
#The program is to display all of these amounts
# ( original food charge, tip, tax and total cost of meal (food charge + tip + tax)).
print ('The Tax and Tip amount is ', Tax_tip)
print (' The Sales tax is ', Tax_amount)
print (' The Sales tip is ', Tip_amount)
print('The Sales Total is ', Total_cost)
