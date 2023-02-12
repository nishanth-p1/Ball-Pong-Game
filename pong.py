# 2 player Ball Pong game made buy Nishanth Pirakalathan
# Run program to play
# Left player controls are W: up, S: down
# Right player controls are Up arrow: up, Down arrow: down


import turtle
import os
 
# Game background
wn = turtle.Screen()
wn.title("background")
wn.bgcolor("pale turquoise")
wn.setup(width=800, height=600)
wn.tracer(0)
 
# Score
leftplayer_score = 0
rightplayer_score = 0

# Game Title
title = turtle.Turtle()
title.color("dark cyan")
title.penup()
title.hideturtle()
title.goto(0, 250)
title.write("Ball Pong Game", align="center", font=("Arial", 28, 'bold', 'italic'))
 
# Score
pen = turtle.Turtle()
pen.color("dark cyan")
pen.penup()
pen.hideturtle()
pen.goto(0, 220)
pen.write("Left Player: 0  Right Player: 0", align="center", font=("Arial", 20, 'italic'))
 
# Box A
leftbox = turtle.Turtle()
leftbox.shape("square")
leftbox.color("dark cyan")
leftbox.speed(0)

leftbox.shapesize(stretch_wid=5,stretch_len=1)
leftbox.penup()
leftbox.goto(-350, 0)
 
# Box B
rightbox = turtle.Turtle()
rightbox.shape("square")
rightbox.color("dark cyan")
rightbox.speed(0)

rightbox.shapesize(stretch_wid=5,stretch_len=1)
rightbox.penup()
rightbox.goto(350, 0)
 
# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("gold")
ball.speed(0)

ball.penup()
ball.goto(0, 0)

# Variable for ball position
ball_x_pos = 0.15
ball_y_pos = 0.15
 
# box movement functions:
def leftbox_up():
    y_pos = leftbox.ycor()
    y_pos += 20
    leftbox.sety(y_pos)
 
def leftbox_down():
    y_pos = leftbox.ycor()
    y_pos -= 20
    leftbox.sety(y_pos)
 
def rightbox_up():
    y_pos = rightbox.ycor()
    y_pos += 20
    rightbox.sety(y_pos)
 
def rightbox_down():
    y_pos = rightbox.ycor()
    y_pos -= 20
    rightbox.sety(y_pos)
 
# Keyboard control bindings
wn.listen()
wn.onkeypress(leftbox_up, "w")
wn.onkeypress(leftbox_down, "s")
wn.onkeypress(rightbox_up, "Up")
wn.onkeypress(rightbox_down, "Down")
 
# Main method to run game
while True:
    wn.update()
   
    # Move the ball
    ball.setx(ball.xcor() + ball_x_pos)
    ball.sety(ball.ycor() + ball_y_pos)
 
    # Boundaries
    if ball.ycor() > 290:
        ball.sety(290)
        ball_y_pos *= -1
        os.system("afplay bounce.wav&")
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball_y_pos *= -1
        os.system("afplay bounce.wav&")
 
    if ball.xcor() > 350:
        leftplayer_score += 1
        pen.clear()
        pen.write("Left Player: {}  Right Player: {}".format(leftplayer_score, rightplayer_score), align="center", font=("Arial", 20, 'italic'))
        ball.goto(0, 0)
        ball_x_pos *= -1
    elif ball.xcor() < -350:
        rightplayer_score += 1
        pen.clear()
        pen.write("Left Player: {}  Right Player: {}".format(leftplayer_score, rightplayer_score), align="center", font=("Arial", 20, 'italic'))
        ball.goto(0, 0)
        ball_x_pos *= -1
 
    # Box and Ball contact
    if (ball.xcor() < -340 and ball.ycor() < leftbox.ycor() + 50 and ball.ycor() > leftbox.ycor() - 50):
        ball_x_pos *= -1
        os.system("afplay bounce.wav&")
   
    elif (ball.xcor() > 340 and ball.ycor() < rightbox.ycor() + 50 and ball.ycor() > rightbox.ycor() - 50):
        ball_x_pos *= -1
        os.system("afplay bounce.wav&")