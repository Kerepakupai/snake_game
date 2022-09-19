from tkinter import RIGHT
from turtle import Turtle


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
	
	def __init__(self) -> None:
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]
	
	def create_snake(self) -> None:
		for position in STARTING_POSITION:
			new_segment = Turtle("square")
			new_segment.color("white")
			new_segment.penup()
			new_segment.goto(position)
			self.segments.append(new_segment)
	
	def move(self) -> None:
		for seg_index in range(len(self.segments)-1, 0, -1):
			new_pos = self.segments[seg_index-1].pos()
			self.segments[seg_index].goto(new_pos)
		
		self.head.forward(MOVE_DISTANCE)

	def up(self) -> None:
		if self.head.heading() != DOWN: 
			self.head.seth(UP)

	def down(self) -> None:
		if self.head.heading() != UP: 
			self.head.seth(DOWN)

	def left(self) -> None:
		if self.head.heading() != RIGHT: 
			self.head.seth(LEFT)
	
	def right(self) -> None:
		if self.head.heading() != LEFT: 
			self.head.seth(RIGHT)