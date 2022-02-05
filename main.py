from turtle import Screen
from turtle import Turtle
from paddle_1 import Paddle_1
from paddle_2 import Paddle_2
import math
from ball import Ball

# screen will be written here
# score of both sides will be increased and displayed here

window = Screen()

window.update()
window.tracer(1)
window.title("Pong")

window.bgcolor("black")
window.setup(800, 600)
dot = Turtle()
dot.color("white")
dot.hideturtle()
dot.pensize(5)
lpaddle = Paddle_1()
rpaddle = Paddle_2()

window.onkeypress(lpaddle.move_up, "Up")
window.onkeypress(rpaddle.move_up, "w")
window.onkeypress(lpaddle.move_down, "Down")
window.onkeypress(rpaddle.move_down, "s")
window.listen()

for i in range(-300, 350, 15):
    if dot.isdown() == False:
        dot.pendown()
        dot.goto(0, i)
    elif dot.isdown() == True:
        dot.penup()
        dot.goto(0, i)

ball = Ball()
# anotherone=Ball()
# anotherone=ball.create_ball()
the_ball = ball.create_ball()

turnt = False
score1 = 0
score2 = 0
bounce_counter = 0
while the_ball.xcor() < 400 and the_ball.xcor() > -400:

    if (ball.ycor() >= 300 or ball.ycor() <= -300) and (bounce_counter == 1 or turnt == True):

            turnt, bounce_counter = ball.bounce_back()
            print(f"{turnt}\n\n")

    elif bounce_counter == 0:
        bounce_counter = ball.movement(turnt)
        print(f"{ball.ball.heading()}\n\n")


    angle = the_ball.heading()
    if (0.0 < math.fabs(
            the_ball.ycor() - lpaddle.paddle.ycor()) < 100.0 and -21.0 < the_ball.xcor() - lpaddle.paddle.xcor() < 21.0):
        the_ball.setheading(180 + angle)
        print("!!!!!!")
        turnt = True
    if (0.0 < math.fabs(
            the_ball.ycor() - rpaddle.paddle.ycor()) < 100.0 and -21.0 < the_ball.xcor() - rpaddle.paddle.xcor() < 21.0):
        the_ball.setheading(180 + angle)
        print("!!!!!!")

        turnt = True

    print((the_ball.xcor(), the_ball.ycor()))
    print((lpaddle.paddle.xcor(), lpaddle.paddle.ycor()))
    print((rpaddle.paddle.xcor(), rpaddle.paddle.ycor()))
    print(ball.ball.heading())
    print(turnt)
    print(bounce_counter)
if ball.xcor() > 400:
    score1 += 1
    lpaddle.score1(score1)

window.exitonclick()
