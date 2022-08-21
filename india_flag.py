import turtle

t = turtle.Turtle()
t.pensize(10)
t.speed(10)
#function to move
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

#Ashok Chakra
t.color("#000080")
for i in range(24):
    t.forward(80)
    t.backward(80)
    t.left(15)
move(0, -80)
t.circle( 80, 360)

#Green
t.begin_fill()
t.color("#006400")
t.forward(350)
t.backward(700)
t.right(90)
t.forward(200)
t.left(90)
t.forward(700)
t.left(90)
t.forward(200)
t.left(90)
t.end_fill()

#orange
t.begin_fill()
t.color("#FBB917")
move(-350, 80)
t.right(180)
t.forward(700)
t.left(90)
t.forward(700)
t.left(90)
t.forward(700)
t.left(90)
t.forward(700)
t.left(90)
t.end_fill()

#only exit when closed
turtle.exitonclick()