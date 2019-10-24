#CONSTANT FOR THE NUMBER OF INCHES PER FOOT.
INCHES_PER_FOOT = 12

#MAIN FUNCTION
def main():
    # GET A NUMBER OF FEET FRROM THE USER.
    feet = int(input('Enter a number of feet: '))

    #conver that to inches.
    print(feet, ' foot equals', feet_to_inches(feet), "inches.")

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

# call the main the functon
main()