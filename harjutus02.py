#Harjutus02 MJ ITS25 09.10.25
import turtle

#konn
turtle.speed(0)
turtle.pensize(6)
screen = turtle.Screen()
screen.title("Olümpia rõngad - Kuusk ITS25")
screen.setup(500,400)

#rõngad
turtle.pencolor("blue")
turtle.penup()
turtle.goto(-105,0)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("black")
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("red")
turtle.penup()
turtle.goto(105,0)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("yellow")
turtle.penup()
turtle.goto(-55,-55)
turtle.pendown()
turtle.circle(50)

turtle.pencolor("green")
turtle.penup()
turtle.goto(55,-55)
turtle.pendown()
turtle.circle(50)

turtle.done()