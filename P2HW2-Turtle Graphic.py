   # Create an shape using python
    # 08/28/2019
    # CTI-110 P2HW2 - Turtle Graphic
    # Michael Fraley
#Pseudocode
#import turtle
#Create a circle
#make turtle go up
#make turtle write north
#make turtle go south
#Make turtle write south
#bring tutrle to center
#Make turtle go east
#make turtle write east
#Make turtle go west
#make turtle write west
    
import turtle
turtle.showturtle()
#Create a circle
turtle.circle(10)
#make turtle go up
turtle.left(90)
turtle.forward(100)
#make turtle write north
turtle.write('North')
#make turtle go south
turtle.setheading(270)
turtle.forward(200)
turtle.penup()
turtle.forward(20)
#Make turtle write south
turtle.write('South')
#bring tutrle to center
turtle.goto(0,10)
turtle.pendown()
#Make turtle go east
turtle.setheading(0)
turtle.setheading(0)
turtle.goto(0,10)
turtle.forward(100)
#make turtle write east
turtle.write('East')
#Make turtle go west
turtle.setheading(180)
turtle.forward(200)
turtle.penup()
turtle.forward(20)
#make turtle write west
turtle.write('West')
