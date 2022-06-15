import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)

# car
car = turtle.Turtle()
car.speed(1)
car.shape("square")
car.color("white")
car.shapesize(stretch_wid=1, stretch_len=2)
car.penup()
car.goto(0, 0)

while True:
    wn.update()
