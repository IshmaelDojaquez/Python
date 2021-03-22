# Pong game

import turtle
import os

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # forces a manual update rather then allowing the window to update on its own

# Score
score_player1 = 0  # player 1
score_player2 = 0  # player 2

# Paddle for player 1
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # size of the paddle
paddle_a.penup()  # makes sure that the paddle is not leaving a trail behind
paddle_a.goto(-350, 0)

# Paddle for player 2
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # size of the paddle
paddle_b.penup()  # makes sure that the paddle is not leaving a trail behind
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()  # makes sure that the ball is not leaving a trail behind
ball.goto(0, 0)  # resets ball to the center of the screen
ball.dx = 0.1  # direction the ball will start on the x coordinate plane
ball.dy = 0.1  # direction the ball will start on the y coordinate plane

# Scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Movement
def paddle_a_up():
    y = paddle_a.ycor()  # current position of the paddle
    y += 20  # how much the paddle will move, either up or down, per press of the button
    paddle_a.sety(y)  # set the new position of the paddle


def paddle_a_down():
    y = paddle_a.ycor()  # current position of the paddle
    y -= 20  # how much the paddle will move, either up or down, per press of the button
    paddle_a.sety(y)  # set the new position of the paddle


def paddle_b_up():
    y = paddle_b.ycor()  # current position of the paddle
    y += 20  # how much the paddle will move, either up or down, per press of the button
    paddle_b.sety(y)  # set the new position of the paddle


def paddle_b_down():
    y = paddle_b.ycor()  # current position of the paddle
    y -= 20  # how much the paddle will move, either up or down, per press of the button
    paddle_b.sety(y)  # set the new position of the paddle


# Keyboard bindings
window.listen()  # "listen" for the key to be called
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Game Loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # updates the movement of the ball in the game
    ball.sety(ball.ycor() + ball.dy)  # updates the movement of the ball in the game

    # Border checking

    # Top and bottom ball
    if ball.ycor() > 290:  # hits the border at 290
        ball.sety(290)  # resets the ball at 290
        ball.dy *= -1  # reverses the direction of the ball

    elif ball.ycor() < -290:  # hits the border at -290
        ball.sety(-290)  # resets the ball at -290
        ball.dy *= -1  # reverses the direction of the ball

    # Top and bottom paddle a
    if paddle_a.ycor() > 250:  # hits the border at 250
        paddle_a.sety(250)  # resets the paddle at 250 so it cant go past it

    elif paddle_a.ycor() < -250:  # hits the border at -250
        paddle_a.sety(-250)  # resets the paddle at -250 so it cant go past it

    # Top and bottom paddle b
    if paddle_b.ycor() > 250:  # hits the border at 250
        paddle_b.sety(250)  # resets the paddle at 250 so it cant go past it

    elif paddle_b.ycor() < -250:  # hits the border at -250
        paddle_b.sety(-250)  # resets the paddle at -250 so it cant go past it

    # Left and right
    if ball.xcor() > 350:
        score_player1 += 1  # add score to player 1
        scoreboard.clear()  # clear board
        scoreboard.write("Player A: {}  Player B: {}".format(score_player1, score_player2), align="center", font=("Courier", 24, "normal"))  # reset board with new values
        ball.goto(0, 0)  # reset ball to center
        ball.dx *= -1  # resets the ball back with a reverse direction on the x coordinate plane

    elif ball.xcor() < -350:
        score_player2 += 1  # add score to player 2
        scoreboard.clear()  # clear board
        scoreboard.write("Player A: {}  Player B: {}".format(score_player1, score_player2), align="center", font=("Courier", 24, "normal"))  # resets board with new values
        ball.goto(0, 0)  # reset ball to center
        ball.dx *= -1  # resets the ball back with a reverse direction on the x coordinate plane

    # Ball hits the paddle
    if ball.xcor() < -340 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:  # player1 paddle
        ball.dx *= -1  # reverses direction of the ball

    elif ball.xcor() > 340 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:  # player2 paddle
        ball.dx *= -1  # reverses the direction of the ball
