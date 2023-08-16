import time

from utils import braille
from utils import ansi

def getFilledBoard(len_x, len_y, value):
	board = []
	for y in range(0, len_y):
		line = []
		for x in range(0, len_x):
			line.append(value)
		board.append(line)
	return board

def filledBoard(len_x=180, len_y=100, wait_time=0.01):
	giga_line = []
	giga_board = []
	for i in range(0, len_x):
		giga_line.append(1)
	for i in range(0, len_y):
		giga_board.append(giga_line)

	while True:
		ansi.clearScreen()
		braille.printBoard(giga_board)
		time.sleep(wait_time)
