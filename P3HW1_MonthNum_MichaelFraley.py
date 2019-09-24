# CTI-110
# P3HW1 - Month number
# Michael Fraley
# 08/29/2019

#Pseudocode
#Prompt the user to pick a month number
# declare the months january February" "March"
# declare the months "April" "May" "June" "July" "August"
# declare the months "September" "October" "November" "December"
#Create if statement and return statement
#Display "The month you have chosen is: " monthname


# promp user to pick a month number
num = int(input("choose the month number:  "))
# create a table for the months
def month_name (number):
    if number == 1:
        return "January"
    elif number == 2:
        return "February"
    elif number == 3:
        return "March"
    elif number == 4:
        return "April"
    elif number == 5:
        return "May"
    elif number == 6:
        return "June"
    elif number == 7:
        return "July"
    elif number == 8:
        return "August"
    elif number == 9:
        return "September"
    elif number == 10:
        return "October"
    elif number == 11:
        return "November"
    elif number == 12:
        return "December"



# Display number asked
print ("The month you have chosen is", month_name (num))
