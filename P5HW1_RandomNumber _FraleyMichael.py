# A brief description of the project
# Date
# CTI-110 P5HW1 - Random Number
# Your Name
#


import random  # Bring in random generator

guessesTaken = 0  # Define the amount of guesses taken
loop = "y"  # define loops, Global value


def mainMenu():
    print("MAIN MENU")  # Creating game screen
    print("------------")  # Creating game screen
    print("")  # Creating game screen
    print("1) Play Game")  # Creating game screen
    print("2) Exit")  # Creating game screen
    option = int(input("Choose which option you would like to choose: "))  # input from users, to make decision
    if option == 1:  # defining what happens for if statement choice 1
        choice1()  # calling function
    else:  # else statment to end game with message
        exit()  # end message but offers to try again


def choice1():  # creating my choice 1 function
    guessesTaken = 0
    while guessesTaken < 5:  # while guess are less than 6 statment
        print('Im thinking of a number 1 - 100. If you guess it right you win, '
              'but if you lose you will have to start over.'
              ' you have 5 trys, lets go!')  # action for guesses < 6
        guess = input()  # define guess as input from user
        guess = int(guess)  # set guess as a integer

        guessesTaken = guessesTaken + 1  # algorithm for adding up guesses taken
        if guess < number:  # first if statement, if less than we will print number guessed to low
            print('YOur guess is too low')  # print too low
        elif guess > number:  # second if statement, if guess is greater than the number -> to high
            print('Your guess is too high.')  # print too high
        elif guess == number:  # anything else we break off the function
            print(" congratulations you win!")
            break


number = random.randint(1, 100)  # our random number choices


def loop1():
    while loop == "y":  # allowing function loop to start
        mainMenu()  # call function


loop1()
