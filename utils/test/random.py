import random

from utils import braille
from utils import ansi


def getRandomBoard(len_x, len_y):
	random_board = []
	for y in range(0, len_y):
		line = []
		for x in range(0, len_x):
			line.append(random.getrandbits(1))
		random_board.append(line)
	return random_board

def randomBoard(len_x=1260, len_y=600):
	while True:
		ansi.clearScreen()
		braille.printBoard(getRandomBoard(len_x, len_y))


