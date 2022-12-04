import turtle

screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=1000, height = 600)

# Paddles + Ball

rightSide = turtle.Turtle()
rightSide.speed(0)
rightSide.shape("square")
rightSide.color("white")
rightSide.shapesize(stretch_wid=6, stretch_len=2)
rightSide.penup()
rightSide.goto(400, 0)


leftSide = turtle.Turtle()
leftSide.speed(0)
leftSide.shape("square")
leftSide.color("white")
leftSide.shapesize(stretch_wid=6, stretch_len=2)
leftSide.penup()
leftSide.goto(-400, 0)

pongBall = turtle.Turtle()
pongBall.speed(40)
pongBall.shape("circle")
pongBall.color("gray")
pongBall.penup()
pongBall.goto(0, 0)
pongBall.dx = 5
pongBall.dy = -5

# Scoreboard
playerOne = 0
playerTwo = 0

scores = turtle.Turtle()
scores.speed(0)
scores.color("pink")
scores.penup()
scores.hideturtle()
scores.goto(0, 260)
scores.write("Player One : 0    Player Two: 0",
             align="center", font=("Arial", 24, "normal"))


# Paddle Movement

def paddleLeftUp():
    y = leftSide.ycor()
    y += 20
    leftSide.sety(y)

def paddleLeftDown():
    y = leftSide.ycor()
    y -= 20
    leftSide.sety(y)

def paddleRightUp():
    y = rightSide.ycor()
    y += 20
    rightSide.sety(y)

def paddleRightDown():
    y = rightSide.ycor()
    y -= 20
    rightSide.sety(y)


# Keyboard

screen.listen()
screen.onkeypress(paddleLeftUp, "w")
screen.onkeypress(paddleLeftDown, "s")
screen.onkeypress(paddleRightUp, "Up")
screen.onkeypress(paddleRightDown, "Down")

