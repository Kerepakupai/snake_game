from turtle import Turtle, Screen
import time

from snake import Snake

if __name__ == "__main__":
	screen = Screen()
	screen.setup(width=600, height=600)
	screen.bgcolor("black")
	screen.title("The Funniest Snake Game")
	screen.tracer(0)

	snake = Snake()

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

	screen.exitonclick()
