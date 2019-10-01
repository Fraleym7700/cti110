# Calculate the total amount and tip amount
#08/28/2019
#CTI-110 P2HW1 - Meal Tip Tax Calculator
# Michael Fraley

# 3. Ask user to enter the charge for food
# 4. Ask user to enter theTip for server ( remember this is a percentage , the input therefore should be decimal. For example,  for a 15% tip, 0.15 should be entered)
# 5. Ask user to enter the Tax amount ( this is a percentage too, so for a 6% tax , 0.06 should be entered)
# 6. Calculate tip and tax
# 7. Display the following:
#    *Calculated tip
#    *Calculated tax
#    *Display total cost of meal ( food charge + tip+ tax)
# 8. Submit your finished code solution file(s) through this assignment link by the posted deadline
# the tip , tax and amount are to be requested from the user, they are NOT hard coded (fixed amounts)
# Write program Pseudocode ( detail algorithm) and add it as a comment block to the submitted program. ( 10 points)


#Pseudocode
#Declare float variables: Charge of the food, Tip, Tax amount
#Display "Enter the price of the ## ITem" where ## is the number
#ask for the tip to server
#Allow choice for 16% for 18% and for 20%
#Calculate the tip and tax
#salestotal = original_price + Tax_amount + Tip_amount
#Display the tip, tax, and sales total)


original_price = float(input("Enter the item's Original Price:$   "))#Ask for the price of food
tip_percentage = ("What tip percentage would you like to choose 16%, 18% and 20%: ")#ask for the tip to server
if tip_percentage == "16":
    tip_amount = original_price * tip_percentage  # define math
    tax_amount = original_price * tax  # define math
    sales_total = original_price + Tax_amount + Tip_amount  # definemath
    print(' The Tip amount is $', format(tip, '.2f'), ".", sep='')  # Display the tip, tax, and sales total)
    print(' The sale tax is $', format(Tax_amount, '.2f'), ".", sep='')  # Display the tip, tax, and sales total)
    print('The Sale Total is $', format(sales_total, '.2f'), ".", sep='')  # Display the tip, tax, and sales total)
elif tip_percentage == "18":
    tip_amount = original_price * tip_percentage  # define math
    tax_amount = original_price * tax  # define math
    sales_total = original_price + Tax_amount + Tip_amount  # definemath
    print(' The Tip amount is $', format(tip, '.2f'), ".", sep='')  # Display the tip, tax, and sales total)
    print(' The sale tax is $', format(Tax_amount, '.2f'), ".", sep='')  # Display the tip, tax, and sales total)
    print('The Sale Total is $', format(sales_total, '.2f'), ".", sep='')  # Display the tip, tax, and sales total)
elif tip_percentage == "20":
    tip_amount = original_price * tip_percentage  # define math
    tax_amount = original_price * tax  # define math
    sales_total = original_price + Tax_amount + Tip_amount  # definemath
    print(' The Tip amount is $', format(tip, '.2f'), ".", sep='')  # Display the tip, tax, and sales total)
    print(' The sale tax is $', format(Tax_amount, '.2f'), ".", sep='')  # Display the tip, tax, and sales total)
    print('The Sale Total is $', format(sales_total, '.2f'), ".", sep='')  # Display the tip, tax, and sales total)
else:
    print("Please choose the selected choices")




