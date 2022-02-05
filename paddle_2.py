from turtle import Turtle
class Paddle_2():
    def __init__(self):
        self.paddle = Turtle()
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.penup()
        self.paddle.setheading(90)
        self.paddle.speed(20)
        self.paddle.shapesize(stretch_len=5, stretch_wid=1)
        self.paddle.setposition(380, 0)

    def move_up(self):
      if self.paddle.ycor() < 230:
        if self.paddle.heading() == 270:
            self.paddle.hideturtle()
            self.paddle.setheading(90)
            self.paddle.showturtle()
        self.paddle.forward(20)

    def move_down(self):
      if self.paddle.ycor() > -230:
        if self.paddle.heading() == 90:
            self.paddle.hideturtle()
            self.paddle.setheading(270)
            self.paddle.showturtle()
        self.paddle.forward(20)

    def score2(self):
        score = Turtle()
