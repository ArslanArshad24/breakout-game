from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.bgcolor("black")
screen.tracer(0)

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("yellow")
        self.shape("square")
        self.shapesize(stretch_len=6, stretch_wid=1)
        self.penup()
        self.goto(position)
    def go_right(self):
        new_x = self.xcor() + 30
        if new_x < 370:
            self.goto(new_x, self.ycor())
    def go_left(self):
        new_x = self.xcor() - 30
        if new_x > -370:
            self.goto(new_x, self.ycor())
         
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.x_move = random.choice([-10, 10]) 
        self.y_move = random.choice([-10, 10])
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_y()
class tried_left(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.chances=3
        self.update()
    def update(self):
        self.clear()
        self.penup()
        self.goto(0,250)
        self.pendown()
        if self.chances >0:
            self.write(f'Chances:{self.chances}',align="center", font=("Courier" , 20, "normal"))
        else:
            self.game_over()
    
    def chances_down(self):
        self.chances -=1
        self.update()
    def game_over(self):
        self.color('red')
        self.write(f'Game Over',align="center", font=("Courier" , 20, "normal"))
        
colors=['yellow','red','green','white','orange','blue','pink','purple']

class Bricks():
    def __init__(self):
        self.all_bricks=[]
        self.x_axis=360
        self.y_axis=40
    def create_bricks(self):
        for line in range(8):
            for brick in range(13):   
                new_brick=Turtle("square")
                new_brick.shapesize(stretch_wid=1,stretch_len=3)
                new_brick.color(random.choice(colors))
                new_brick.penup()
                new_brick.goto(self.x_axis,self.y_axis)
                self.all_bricks.append(new_brick)
                self.x_axis=self.x_axis-61
            self.x_axis=360
            self.y_axis=self.y_axis-22

    def remove_brick(self,current_brick):
        current_brick.hideturtle()
        self.all_bricks.remove(current_brick)
        
paddle = Paddle((0, -280))
screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

ball = Ball()
try_now = tried_left()

brick=Bricks()
brick.create_bricks()

game_on=True
while game_on:
    ball.move()
    if ball.distance(paddle) < 30 or ball.ycor() > 295:
        ball.bounce_y()

    if ball.xcor() > 395 or ball.xcor() < -395:
        ball.bounce_x()
    
    if ball.ycor() < -330:
        ball.reset_position()
        try_now.chances_down()
        if try_now.chances <= 0:
            game_on=False
    
    for current_brick in brick.all_bricks:
        if ball.distance(current_brick) < 25:
            ball.bounce_y()
            brick.remove_brick(current_brick)
        
    if not brick.all_bricks:
        game_on = False
        try_now.color('green')
        try_now.penup()
        try_now.goto(0, 0)
        try_now.pendown()
        try_now.write('You Win!', align="center", font=("Courier", 24, "normal"))
    
    screen.update()
    time.sleep(ball.move_speed)

screen.exitonclick()



