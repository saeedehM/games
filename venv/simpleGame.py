import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=200,height=200,startx=10,starty=-200)
wn.tracer(0)

while True:
    wn.update()