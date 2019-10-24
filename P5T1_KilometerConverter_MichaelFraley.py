# Create a function that translate kilometers to miles.
# 10/17/2019
# CTI-110 P5T1_KilometerConverter
# Michael Fraley
#
CONVERSION_FACTOR = 0.6214
def main():
    #Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    #Display the distance converted to miles.
    show_miles(kilometers)

def show_miles(km):
    #calculate miles.
    miles = km * CONVERSION_FACTOR

    #display the miles.
    print(km, 'kilometers equal', miles, "miles.")

#call the main function.
main()