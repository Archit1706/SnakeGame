import turtle
from turtle import Turtle, Screen
import time
from food import Food
from snake import Snake
from score_board import ScoreBoard
from border import Border

game_is_on = True


# def stop_game():
#     global game_is_on
#     game_is_on = False
#     return True


screen = Screen()
screen.setup(width=620, height=620)
screen.bgcolor("green")
screen.title("Snake Game")

screen.tracer(0)
border = Border()

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# screen.onkey(stop_game, "s")

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score(score_board.score)
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        # score_board.game_over()
        score_board.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            # game_is_on = False
            # score_board.game_over()
            snake.reset()

    # if stop_game():
    #     print("Thankyou!")
screen.exitonclick()
