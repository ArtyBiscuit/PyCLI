#!/usr/bin/env python3

from utils import braille
from utils import ansi
from utils import TMP_DIR

import sys
import time
import random

from pprint import pprint

# TEST ZONE

## RANDOM STUFF
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
		board = getRandomBoard(len_x, len_y)
		braille.printBoard(board)

## FILLED BOARD
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

## SPINNING CROSS
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

if __name__ == "__main__":
	# spinningCross()
	# randomBoard(1, 1)
	# randomBoard(4, 4)
	# randomBoard(50, 50)
	# filledBoard(400, 200)

	# braille.printImg(sys.argv[1])

	# board = braille.img2Braille(TMP_DIR + "smoll.png")
	# braille.printBraille(board)

	# braille.braille2File(board, "proto.bim")

	# board_from_file = braille.file2Braille("proto.bim")

	# braille.printBraille(board_from_file)

	boards = braille.file2BrailleVid("proto.bvi")
	for board in boards:
		ansi.clearScreen()
		braille.printBraille(board)
		time.sleep(1 / 30)
