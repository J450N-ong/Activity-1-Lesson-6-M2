import turtle
sc = turtle.Screen()
sc.bgcolor('lightblue')
sc.setup(300,400)
pen = turtle.Turtle()

no = int(input("Enter the number of sides of a polygon: "))
sl = int(input("Enter the length of the sides: "))
angle = 360/no

for i in range(no):
    pen.forward(sl)
    pen.right(angle)

turtle.done()