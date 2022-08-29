from turtle import Screen
import paddle
import time
import ball
import score

scores = score.scoreboard()

# response = input("Do you want to play in Full-screen?, Y or N : ")

screen = Screen()
screen.screensize(canvwidth=500, canvheight=500)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

right_paddle = paddle.Paddle("right")
left_paddle = paddle.Paddle("left")

screen.update()

circle = ball.Ball()

game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")
    screen.onkey(left_paddle.up, "w")
    screen.onkey(left_paddle.down, "s")
    screen.tracer(0)
    screen.update()
    time.sleep(0.1)
    circle.move()
    circle.detect_collision()
    if circle.xcor() >= 375:
        circle.reset()
        scores.lscore += 1
        scores.update_score()

    elif circle.xcor() <= -380:
        scores.rscore += 1
        scores.update_score()
        circle.reset()

    if circle.xcor() >= 340 and circle.ycor() - right_paddle.paddy.ycor() < 40:
        circle.bounce('x')
    print(left_paddle.paddy.xcor())
    print(left_paddle.paddy.ycor())
    if circle.xcor() <= -346 and (circle.ycor() - left_paddle.paddy.ycor() < 40):
        print("hello world")
        circle.bounce('x')

screen.exitonclick()
