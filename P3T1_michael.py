#Write a program that asks for the length and width of two rectangles.
# The program should tell the user which rectangle has the greater area, or if the two rectangles have equal area.
#As always, you should begin with the appropriate comment block.
#Write the program, test it, and submit it through Blackboard. Finally, upload the file to your online repository.
#Write a program that asks for the length and width of two rectangles.
# The program should tell the user which rectangle has the greater area, or if the two rectangles have equal area.
#As always, you should begin with the appropriate comment block.
#Write the program, test it, and submit it through Blackboard. Finally, upload the file to your online repository.

#psedocode
#1. define my variables for length and with of both rectangles
#2.Define the equation L * W = A
#create if statement for choosing rectangle
#display which rectangle is better

length1 = int(input("Enter the length of the rectangle 1 "))
width1 = int(input(("Enter the width of the rectangle 1 "))

length2 = int(input("Enter the length of the rectangle 2 "))
width2 = int(input("Enter the width of the rectangle 2 "))

area1 = length1 * width1
area2 = length2 * width2

if area1 > area2:
    print('Rectangle 1 has the greater area. ')
elif area2 > area1:
    print('Rectanglle has the greater area. ')
else:
    print('Both have the same area.')
