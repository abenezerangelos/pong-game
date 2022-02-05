from turtle import Turtle
import random
import math
from paddle_1 import Paddle_1
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball=Turtle()
        self.c=0

    def create_ball(self):
        y=random.randint(-290,290)

        self.ball.shape("circle")
        self.ball.penup()
        self.ball.color("white")
        self.ball.speed(20)

        self.ball.setposition(0,y)
        dist1=self.ball.distance(0,230)
        dist2=self.ball.distance(0,-230)
        angle1=math.degrees(math.atan(400/dist1))
        angle2=math.degrees(math.atan(400/dist2))
        possible_list_of_angles=[random.randint(1,int(angle1)),random.randint(180-int(angle1),179),random.randint(int(-1*angle2),-1),random.randint(-179,-180+int(angle2))]
        self.c=random.choice(possible_list_of_angles)
        total_angle=angle1+angle2
        self.ball.setheading(self.c)

        print(angle1)
        print(angle2)
        print(total_angle)
        print(180-total_angle)
        print(self.c)
        return self.ball


    def movement(self,turnt):
     if self.ball.ycor()<300 and self.ball.ycor()>-300:
        self.ball.forward(5)
     elif self.ball.ycor()>=300 or self.ball.ycor()<=-300:

      if turnt==False:
        self.ball.setheading(-1*self.c)
        self.ball.forward(10)
        print("what is wrong")
      else:
          pass
      return 1
     return 0

    def bounce_back(self):
        self.ball.setheading(-1*self.ball.heading())
        self.ball.forward(50)
        print("$$$$$$$")
        return False,0







