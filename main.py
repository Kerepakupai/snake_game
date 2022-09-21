from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard



if __name__ == "__main__":
	screen = Screen()
	screen.setup(width=600, height=600)
	screen.bgcolor("black")
	screen.title("The Funniest Snake Game")
	screen.tracer(0)

	snake = Snake()
	food = Food()
	scoreboard = Scoreboard()

	screen.listen()
	screen.onkey(snake.up, "Up")
	screen.onkey(snake.down, "Down")
	screen.onkey(snake.left, "Left")
	screen.onkey(snake.right, "Right")

	is_game_on = True
	while is_game_on:
		time.sleep(0.2)
		screen.update()
		snake.move()

		# Detect collision with food
		if snake.head.distance(food) < 15:
			food.refresh()
			snake.extend()
			scoreboard.increse_score()

		# Detect collision with wall
		if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
			is_game_on = False
			scoreboard.game_over()

		# Detect collision wiyh tail
		for segment in snake.segments[1:]:
			if snake.head.distance(segment) < 10:
				is_game_on = False
				scoreboard.game_over()

	screen.exitonclick()
