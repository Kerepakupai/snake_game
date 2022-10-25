from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Arial", 12, "bold")


class Scoreboard(Turtle):

	def __init__(self) -> None:
		super().__init__()
		self.score = 0
		self.high_score = self.get_high_score()
		self.penup()
		self.hideturtle()
		self.color("white")
		self.goto(0, 270)
		self.update_scoreboard()
	
	def update_scoreboard(self):
		self.clear()
		self.write(f"Score: {self.score}   High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

	def increase_score(self):
		self.score += 1
		self.update_scoreboard()

	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
			self.set_high_score()
		self.score = 0
		self.update_scoreboard()

	def game_over(self):
		self.goto(0, 0)
		self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

	@staticmethod
	def get_high_score():
		with open("score.txt", mode="r") as file:
			score = file.read()

		return int(score)

	def set_high_score(self):
		with open("score.txt", mode="w") as file:
			file.write(str(self.high_score))
