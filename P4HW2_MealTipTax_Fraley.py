# Calculate the total amount and tip amount
#08/28/2019
#CTI-110
#P4HW2 - MealTipTax
# Michael Fraley

# 3. Ask user to enter the charge for food
# 4. Ask user to enter theTip for server ( remember this is a percentage , the input therefore
# should be decimal. For example,  for a 15% tip, 0.15 should be entered)
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
tax = .06
tip = 0
totalCost = 0
subTotal = 0
loop = "y" #Define the loop


while loop == "y": #Start the loop
    foodCharge = float(input("What was the original price of your meal?: $ ")) #Get cost of the meal
    tipPercentage = float(input("How much would you like to tip, You can tip 16% 18% and 20%: % "))# ask for tip
    tipAmount = (tipPercentage / 100) * foodCharge
    taxAmount = (tax * foodCharge)
    totalCost = (foodCharge + tipAmount + taxAmount)
    if tipPercentage == 16: # print if is 16%
        print('The Tip amount is $', format(tipAmount, '.2f'), ".", sep='')  # Display the tip, tax, and sales total)
        print('The sale tax is $', format(taxAmount, '.2f'), ".", sep='')  # Display the tip, tax, and sales total)
        print('The Sale Total is $', format(totalCost, '.2f'), ".", sep='')  # Display the tip, tax, and sales total)
    elif tipPercentage == 18:# print if is 18%
        print('The Tip amount is $', format(tipAmount, '.2f'), ".", sep='')  # Display the tip, tax, and sales total)
        print('The sale tax is $', format(taxAmount, '.2f'), ".", sep='')  # Display the tip, tax, and sales total)
        print('The Sale Total is $', format(totalCost, '.2f'), ".", sep='')  # Display the tip, tax, and sales total)
    elif tipPercentage == 20:# print if is 20%
        print('The Tip amount is $', format(tipAmount, '.2f'), ".", sep='')  # Display the tip, tax, and sales total)
        print('The sale tax is $', format(taxAmount, '.2f'), ".", sep='')  # Display the tip, tax, and sales total)
        print('The Sale Total is $', format(totalCost, '.2f'), ".", sep='')  # Display the tip, tax, and sales total)
    else: #doesn't allow return
        print("please enter the correct percentage value")
    loop = input("Would you like to rerun the program? (y/n): ")
    if loop == "n":
        print("press enter to exit...") #wait for user to exit
