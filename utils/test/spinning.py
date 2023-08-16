import time

from utils import braille
from utils import ansi

def spinningCross(wait_time=0.2):
	xxxs = [
		[1, 0, 1],
		[0, 1, 0],
		[1, 0, 1],
	]
	cross = [
		[0, 1, 0],
		[1, 1, 1],
		[0, 1, 0],
	]
	while True:
		ansi.clearScreen()
		braille.printBoard(xxxs)
		time.sleep(wait_time)
		ansi.clearScreen()
		braille.printBoard(cross)
		time.sleep(wait_time)
