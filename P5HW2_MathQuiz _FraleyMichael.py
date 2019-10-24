# Math quiz
# 10/24/2019
# CTI-110 P5HW2 - Math Quiz
# Michael Fraley
#
#psedocode
#create main menu
#allow user to have options
#if choose 1 it will add a number
#if choose 2 it will subtract a number
#Psedocode
#import random
#Create game format
#allow use 3 options.
#ask user to do quiz
#congratulate if correct or tell them if wrong
#create a check naswer algorithm

import random #importing the randomness

randomNumber1 = random.randint(1,250) #my random number 1
randomNumber2 = random.randint(1, 250)#my random number 2
def main(): # set main function
    gameFormat() #call game format



def gameFormat(): #game format function

    print("\nMAIN MENU") #game design
    print("----------------")#game design
    print("1) Add Random numbers")#game design
    print("2) Subtract Random numbers")#game design
    print("3) Exit the game")#game design
    option = int(input("Choose which option you would like to choose: \n"))  # input from users, to make decision
    if option == 1:  # defining what happens for if statement choice 1
        userAnswer1 = askQuestion1() # calling function 1st question and refering the user's answer
        checkAnswer1(userAnswer1)# calling function for check answer and refers to user answer
        main()
    elif option == 2: # choice 2
        userAnswer2 = askQuestion2()  # calling function 1st question and refering the user's answer
        checkAnswer2(userAnswer2) # calling function for check answer and refers to user answer
        main()
    elif option == 3: #otion 3
        exit #exit


def askQuestion1():
    global randomNumber1 # calling global number
    global randomNumber2 # calling global number
    print(randomNumber1 + randomNumber2) # cheat statement
    userAnswer1 = int(input("What is " + str(randomNumber1) + "+" +\
              str(randomNumber2)+ "?: \n")) # equation
    return userAnswer1 # return answer
def askQuestion2():
    global randomNumber1 # calling global number
    global randomNumber2 # calling global number
    print(randomNumber1 - randomNumber2) # cheat statement
    userAnswer2 = int(input("What is " + str(randomNumber1) + "-" +
              str(randomNumber2)+ "?: \n")) # equation
    return userAnswer2 # return answer
def checkAnswer1(userAnswer ):
    global randomNumber1 # calling global number
    global randomNumber2 # calling global number

    correctAnswer = randomNumber1 +randomNumber2 #correct answer
    if userAnswer == correctAnswer:
        print("\ncongratulations!") # congrats
    else:
        print("It's wrong. The correct answer is", correctAnswer)#you lose
def checkAnswer2(userAnswer ):
    global randomNumber1# calling global number
    global randomNumber2# calling global number

    correctAnswer = randomNumber1 - randomNumber2#correct answer
    if userAnswer == correctAnswer:
        print("\ncongratulations!\n") # congrats
    else:
        print("It's wrong. The correct answer is", correctAnswer)#you lose
main()
