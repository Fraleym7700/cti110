    # Create an shape using python
    # 08/28/2019
    # CTI-110 P2HW2 - Turtle Graphic
    # Michael Fraley

import turtle
turtle.showturtle()

turtle.circle(10)
turtle.left(90)
turtle.forward(100)
turtle.write('North')
turtle.setheading(270)
turtle.forward(200)
turtle.penup()
turtle.forward(20)
turtle.write('South')
turtle.goto(0,10)
turtle.pendown()
turtle.setheading(0)
turtle.setheading(0)
turtle.goto(0,10)
turtle.forward(100)
turtle.write('East')
turtle.setheading(180)
turtle.forward(200)
turtle.penup()
turtle.forward(20)
turtle.write('West')
