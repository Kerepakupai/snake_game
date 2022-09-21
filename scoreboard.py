from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Arial", 12, "bold")

class Scoreboard(Turtle):

	def __init__(self) -> None:
		super().__init__()
		self.score = 0
		self.penup()
		self.hideturtle()
		self.color("white")
		self.goto(0, 270)
		self.update_scoreboard()
	
	def update_scoreboard(self):
		self.clear()
		self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

	def increse_score(self):
		self.score += 1
		self.update_scoreboard()

	def game_over(self):
		self.goto(0, 0)
		self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
