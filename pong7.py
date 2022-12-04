import time
import turtle
def runtime(n):
    runtime = time.time() - n

    mins = runtime // 60
    sec = int(runtime % 60)
    hours = int(mins // 60)
    mins = int(mins % 60)

    elapsed = [hours,mins,sec]
    return elapsed 
    
    
#Background setup
    
screen = turtle.Screen()
screen.title("Pong")
#screen.bgcolor("black")
screen.setup(width=1000, height = 600)

# Paddles + Ball

rightSide = turtle.Turtle()
rightSide.speed(0)
rightSide.shape("square")
rightSide.color("black")
rightSide.shapesize(stretch_wid=6, stretch_len=2)
rightSide.penup()
rightSide.goto(400, 0)


leftSide = turtle.Turtle()
leftSide.speed(0)
leftSide.shape("square")
leftSide.color("black")
leftSide.shapesize(stretch_wid=6, stretch_len=2)
leftSide.penup()
leftSide.goto(-400, 0)


pongBall = turtle.Turtle()
pongBall.speed(0)
pongBall.shape("circle")
pongBall.color("gray")
#pongBall.penup()
pongBall.goto(0, 0)
pongBall.dx = 5
pongBall.dy = -5

# Scoreboard
playerOne = 0
playerTwo = 0
start = time.time()
round_start_time = start
scores = turtle.Turtle()
scores.speed(0)
scores.color("pink")
scores.penup()
scores.hideturtle()
scores.goto(0, 260)
scores.write("Player One : 0    0:0:0    Player Two: 0",align="center"
, font=("Arial", 24, "normal"))


# Paddle Movement

def paddleLeftUp():
    y = leftSide.ycor()
    y += 20
    leftSide.sety(y)

def paddleLeftDown():
    y = leftSide.ycor()
    y -= 20
    leftSide.sety(y)
def paddleLeftRight():
    if not leftSide.xcor() > 0:
        x = leftSide.xcor()
        x += 20
        leftSide.setx(x)

def paddleLeftLeft():
        x = leftSide.xcor()
        x -= 20
        leftSide.setx(x)

def paddleRightUp():
    y = rightSide.ycor()
    y += 20
    rightSide.sety(y)

def paddleRightDown():
    y = rightSide.ycor()
    y -= 20
    rightSide.sety(y)
    
def paddleRightLeft():
    if not rightSide.xcor() < 0:
        x = rightSide.xcor()
        x -= 20
        rightSide.setx(x)

def paddleRightRight():
    x = rightSide.xcor()
    x += 20
    rightSide.setx(x)

# Keyboard

screen.listen()
screen.onkeypress(paddleLeftUp, "w")
screen.onkeypress(paddleLeftLeft, "a")
screen.onkeypress(paddleLeftRight, "d")
screen.onkeypress(paddleLeftDown, "s")
screen.onkeypress(paddleRightUp, "Up")
screen.onkeypress(paddleRightDown, "Down")
screen.onkeypress(paddleRightLeft, "Left")
screen.onkeypress(paddleRightRight, "Right")

# Ball Borders
while True:
    screen.update()
    clock = runtime(start)
    pongBall.setx(pongBall.xcor()+pongBall.dx)
    pongBall.sety(pongBall.ycor()+pongBall.dy)
   
    if pongBall.ycor() > 280:
        pongBall.sety(280)
        pongBall.dy *= -1
 
    if pongBall.ycor() < -280:
        pongBall.sety(-280)
        pongBall.dy *= -1
 
    if pongBall.xcor() > 500:
        pongBall.goto(0, 0)
        pongBall.dy *= -1
        playerOne += 1
        round_start_time = time.time()
    
    if pongBall.xcor() < -500:
        pongBall.goto(0, 0)
        pongBall.dy *= -1
        playerTwo += 1
        round_start_time = time.time()
        
    scores.clear() 
    scores.write("player One : {}    {}    player Two: {}".format(
                                playerOne, clock, playerTwo), align="center",
                                font=("Arial", 24, "normal"))
    if playerTwo == 15 or playerOne == 15:
        break

# Ball Collision w/ Paddles
    if (pongBall.xcor() > rightSide.xcor()-30 and pongBall.xcor() < rightSide.xcor()+30) and (pongBall.ycor() < rightSide.ycor()+40 and pongBall.ycor() > rightSide.ycor()-40):
        pongBall.setx(pongBall.xcor())
        pongBall.dx*=-1
        
    if (pongBall.xcor() < leftSide.xcor()+30 and pongBall.xcor() > leftSide.xcor()-30) and (pongBall.ycor() < leftSide.ycor()+40 and pongBall.ycor() > rightSide.ycor()-40):
        pongBall.setx(pongBall.xcor())
        pongBall.dx*=-1

scores.clear()
if playerOne == 15:
    scores.write("player One : {} Winner!   {}    player Two: {}".format(
                                playerOne, clock, playerTwo), align="center",
                                font=("Arial", 24, "normal"))
else:
    scores.write("player One : {}   {}    player Two: {} Winner!".format(
                                playerOne, clock, playerTwo), align="center",
                                font=("Arial", 24, "normal"))

