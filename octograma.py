import turtle

w = turtle.Screen()
w.bgcolor("black")

estrella = turtle.Turtle()

estrella.hideturtle()
estrella.fillcolor("purple")
estrella.pencolor("white")
estrella.pensize(5)

estrella.penup()
estrella.goto(-100, -50)
estrella.pendown()

estrella.begin_fill()
for i in range(8):
    estrella.right(135)
    estrella.forward(-200)

estrella.end_fill()
estrella.showturtle()
turtle.mainloop()
