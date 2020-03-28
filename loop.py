import random
import turtle
import time
import winsound
import tkinter

#convention
x_axes = 600
y_axes = 650

#screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("bg.gif")
wn.setup(width=x_axes, height=y_axes)
wn.title("PONG")
wn.tracer(0)

#scoreboard
board1 = turtle.Turtle()
board1.shape("square")
board1.shapesize(stretch_len=5,stretch_wid= 3)
board1.color("green","black")
board1.hideturtle()
board1.penup()
board1.goto(-130,290)
board1.write("POINT: " ,align = 'right',font=('Serif',12,'bold'))

board2 = turtle.Turtle()
board2.shape("square")
board2.shapesize(stretch_len=5,stretch_wid= 3)
board2.color("green","#ADFF00")
board2.hideturtle()
board2.penup()
board2.goto(110,290)
board2.write("POINT: ",align = 'left',font=('Serif',12,'bold'))

#ball
ball= turtle.Turtle()
ball.shape("circle")
ball.color("#ADFF00","#028900")
ball.penup()
ball.goto(0,0)
ball_speed_x =2
ball_speed_y = 1.5
#paddles
#paddle 1 left
paddleL = turtle.Turtle()
paddleL.shape("square")
paddleL.shapesize(stretch_wid=6,stretch_len=1)
paddleL.color("green","black")
paddleL.penup()
paddleL.goto(x_axes/-2+20,0)

#paddle 2 right
paddleR = turtle.Turtle()
paddleR.shape("square")
paddleR.shapesize(stretch_wid=6,stretch_len=1)
paddleR.color("green","black")
paddleR.penup()
paddleR.goto(x_axes/2-20,0)

#ending the game
ending_point = 300
GameOver =turtle.Turtle()
GameOver.shape("square")
GameOver.shapesize(stretch_wid=3, stretch_len=6)
GameOver.hideturtle()
GameOver.color("green","grey")
GameOver.penup()


#paddel bindings and speed def
paddle_speed = 50
#key bindings
def paddleL_up():
    y=paddleL.ycor()
    y=y+paddle_speed
    paddleL.sety(y)
def paddleL_down():
    y=paddleL.ycor()
    y=y-paddle_speed
    paddleL.sety(y)
def paddleR_down():
    y=paddleR.ycor()
    y=y-paddle_speed
    paddleR.sety(y)
def paddleR_up():
    y=paddleR.ycor()
    y=y+paddle_speed
    paddleR.sety(y)
#pressed keys
wn.listen()
wn.onkeypress(paddleL_up,"z")
wn.onkeypress(paddleL_down,"s")
wn.onkeypress(paddleR_up,"Up")
wn.onkeypress(paddleR_down,"Down")

#points
point_L = 0
point_R = 0
incre = 0

#main loop
while True:
    wn.update()

    #ball movement
    ball.setx(ball.xcor()+ ball_speed_x)
    ball.sety(ball.ycor()+ ball_speed_y)
    #ball bounces on the wall
    if ball.ycor() >= y_axes/2 - 60:
        ball.sety(y_axes/2 -60)
        ball_speed_y = ball_speed_y * -1

    if ball.ycor() <= y_axes/-2 + 30:
        ball.sety(y_axes/-2 +60)
        ball_speed_y = ball_speed_y * -1
    # collision with paddle left
    if (ball.xcor() == paddleL.xcor() + 10 ) : # x axes
        if (ball.ycor() < paddleL.ycor() + 70 and ball.ycor() > paddleL.ycor() - 70): # y axes
            ball_speed_x = ball_speed_x *-1
    #collision with paddle right
    if (ball.xcor() == paddleR.xcor() -10 ) : # x axes
        if (ball.ycor() < paddleR.ycor() + 70 and ball.ycor() > paddleR.ycor() - 70): # y axes
            ball_speed_x = ball_speed_x *-1
    # ball reappears if runs off the left screen
    if ball.xcor() <= - 600:  #left
        ball_speed_x= ball_speed_x*-1
        ball.goto(0,0)
        point_L= point_L + 50
        board2.clear()
        board2.write("POINT: {}" .format(point_L),align = 'left',font=('Serif',13,'bold'))

    if ball.xcor()>=580: # right
        ball_speed_x= ball_speed_x*-1
        ball.goto(0,0)
        point_R= point_R + 50
        board1.clear()
        board1.write("POINT: {}" .format(point_R),align = 'right',font=('Serif',12,'bold'))
    #screen telezorp
    #paddleR
    if paddleR.ycor() > 210 :
        x=paddleR.xcor()
        paddleR.goto(x,-220)
    if paddleR.ycor() < -220 :
        x=paddleR.xcor()
        paddleR.goto(x,210)
    #paddleL
    if paddleL.ycor() > 210 :
        x=paddleL.xcor()
        paddleL.goto(x,-220)
    if paddleL.ycor() < -220 :
        x=paddleL.xcor()
        paddleL.goto(x,210)

    #ending the game
    # if point_L == ending_point or point_R == ending_point :
        # ball_speed_y,ball_speed_y,paddle_speed= 0,0,0

