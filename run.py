#!/usr/bin/env python3

from utils import spinningCross, randomBoard, filledBoard, fromImg

import sys

if __name__ == "__main__":
	# spinningCross()
	# randomBoard(4, 4)
	# filledBoard(400, 200)
	fromImg(sys.argv[1])