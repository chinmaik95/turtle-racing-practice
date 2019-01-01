import turtle as t
from random import randint

t.speed(10)
t.penup()
t.goto(-140,140) # Coordinates of the turtle

for i in range(15):      #for each step
    t.write(i, align="center")          # for each iteration
    t.right(90)         # tilt the head to right
    t.forward(10)       # leave gap between the number and line

    for j in range(8):
        t.pendown()  # click of pen
        t.forward(10)      # draw a line forward
        t.penup()           # not drawing anymore
        t.forward(10)
    t.backward(170)
    t.left(90)
    t.forward(20)

ada = t.Turtle()
ada.color("red")
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.pendown()


bob = t.Turtle()
bob.color("blue")
bob.shape('turtle')
bob.penup()
bob.goto(-160,70)
bob.pendown()


cat = t.Turtle()
cat.color("yellow")
cat.shape('turtle')
cat.penup()
cat.goto(-160,40)
cat.pendown()

for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    cat.forward(randint(1, 5))

for turn in range(1):
        ada.right(180)
        bob.right(180)
        cat.right(180)


for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    cat.forward(randint(1, 5))

if ada.currentLine == 1:
    print("Color red is the winner")