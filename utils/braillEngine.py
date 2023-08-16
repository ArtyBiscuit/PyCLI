import cv2

EXT_IMG = ".bim" # braille image
EXT_VID = ".bvi" # braille video

class Board():
	pass

class BraillEngine():
	"""
	Class
	-----
	Engine to render images with the braille characters (0x2800-0x28FF)

	board: a 2D array of boolean

	charmap: the converted 2D unicode char from the board

	Attributes
	----------
	braille_base : int, optional
		the base of the unicode braille char (default 0x2800)
	braille_len_x : str, optional
		the x axis len of a braille char, based on the first line of the board (default 2)
	braille_len_y : str, optional
		the y axis len of a braille char (default 4)

	Methods
	-------
	getTile(board, base)
		Get a tile of 2x4 of a board, given a base, and append it to the current
		self.line

	board2Braille(board)
		Take a board and convert it to a charmap

	img2Board(path)
		Convert an image file to a board

	img2Braille(path)
		Convert an image file to a charmap

	printBoard(board)
		Convert a board to a charmap then print it

	printBraille(charmap)
		Print a charmap

	printImg(path)
		Print an image with braille char, given a path for the image

	braille2File(board, file_path)
	"""

	def __init__(self,
			braille_base = 0x2800,
			braille_len_x = 2,
			braille_len_y = 4):
		self.braille_base = braille_base
		self.braille_len_x = braille_len_x
		self.braille_len_y = braille_len_y

	# CORE

	def	getTile(self, board, base):
		"""
		getTile
		-------
		Get a tile of 2x4 of a board, given a base, and append it to the current
		self.line

		Parameters
		----------
		board :
			The board to choose the tile from
		base : (int, int)
			The base, x and y of the tile
		"""
		tmp_char = 0
		try:
			if (board[base[0]][base[1]]):
				tmp_char |= 1 << 0
				color = board[base[0]][base[1]]
			if (board[base[0] + 1][base[1]]):
				tmp_char |= 1 << 1
				color = board[base[0] + 1][base[1]]
			if (board[base[0] + 2][base[1]]):
				tmp_char |= 1 << 2
				color = board[base[0] + 2][base[1]]
			if (board[base[0] + 3][base[1]]):
				tmp_char |= 1 << 6
				color = board[base[0] + 3][base[1]]
		except IndexError:
			pass
		try:
			if (board[base[0]][base[1] + 1]):
				tmp_char |= 1 << 3
				color = board[base[0]][base[1] + 1]
			if (board[base[0] + 1][base[1] + 1]):
				tmp_char |= 1 << 4
				color = board[base[0] + 1][base[1] + 1]
			if (board[base[0] + 2][base[1] + 1]):
				tmp_char |= 1 << 5
				color = board[base[0] + 2][base[1] + 1]
			if (board[base[0] + 3][base[1] + 1]):
				tmp_char |= 1 << 7
				color = board[base[0] + 3][base[1] + 1]
		except IndexError:
			pass
		self.line.append(chr(self.braille_base + tmp_char))

	def board2Braille(self, board):
		"""
		board2Braille
		-------------
		Take a board and convert it to a charmap

		Parameters
		----------
		board :
			The board to print

		Returns
		-------
		The converted charmap.
		"""
		len_y = len(board)
		len_x = len(board[0])
		len_y = int(len_y / self.braille_len_y) + ((len_y % self.braille_len_y) != 0)
		len_x = int(len_x / self.braille_len_x) + ((len_x % self.braille_len_x) != 0)
		self.converted = []
		for y in (range(len_y)):
			self.line = []
			for x in (range(len_x)):
				self.getTile(board, (y * self.braille_len_y, x * self.braille_len_x))
			self.converted.append(self.line)
		return self.converted

	# IMG UTILS

	def img2Board(self, path):
		"""
		img2Board
		---------
		Convert an image file to a board

		Parameters
		----------
		path : str
			The file to convert.

		Returns
		-------
		The converted board.
		"""
		# load the input image
		img = cv2.imread(path)

		# convert the input image to grayscale
		img_data = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		# apply thresholding to convert grayscale to binary image
		board = cv2.threshold(img_data,127,255,cv2.THRESH_BINARY)[1]
		# board = cv2.threshold(img_data,0,127,cv2.THRESH_BINARY)[1]
		return (board)

	def img2Braille(self, path):
		"""
		img2Braille
		-----------
		Convert an image file to a charmap

		Parameters
		----------
		path : str
			The file to convert.

		Returns
		-------
		The converted charmap.
		"""
		return (self.board2Braille(self.img2Board(path)))

	# PRINT UTILS

	def printBoard(self, board):
		"""
		printBoard
		------------
		Convert a board to a charmap then print it

		Parameters
		----------
		board : str
			The board to print
		"""
		charmap = self.board2Braille(board)
		for line in charmap:
			print(''.join(line))

	def printBraille(self, charmap):
		"""
		printBraille
		------------
		Print a charmap

		Parameters
		----------
		board : str
			The charmap to print
		"""
		for line in charmap:
			print(''.join(line))

	def printImg(self, path):
		"""
		printImg
		--------
		Print an image with braille char, given a path for the image

		Parameters
		----------
		path : str
			The file to print.
		"""
		self.printBoard(self.image2Board(path))

	# FILE MANAGEMENT

	def braille2File(self, board, file_path):
		"""
		braille2File
		------------
		Convert charmap into a file, with extension .bim (braille image)

		Parameters
		----------
		path : str
			The path of the converted file. without .bim.
		"""
		to_write = []

		for y in range(len(board)):
			for x in range(len(board[0])):
				to_write.append(f"{ord(board[y][x]) & 0b1111_1111:02x}")
			to_write.append('\n')
		with open(file_path, "w") as f:
			f.write(''.join(to_write))

	def file2Braille(self, file_path):
		"""
		braille2File
		------------
		Convert a .bim file into charmap

		Parameters
		----------
		file_path : str
			The file path to convert

		Returns
		-------
		The parsed charmap.
		"""
		board = self.file2BrailleVid(file_path)
		if len(board) == 0:
			print("error converting file")
			exit(12)
		return (board[0])

	def file2BrailleVid(self, file_path):
		"""
		file2BrailleVid
		---------------
		Convert a .bvi file (.bim, because they parsed the same) into charmap

		Parameters
		----------
		file_path : str
			The file to convert

		Returns
		-------
		The parsed charmap scene.
		"""
		with open(file_path, "r") as f:
			file_str = f.read()
		scenes = []
		scene = []
		lines = file_str.split('\n')
		lines_nb = len(lines)

		for i in range(lines_nb):
			if len(lines[i]) == 0:
				scenes.append(scene)
				scene = []
				continue
			line = [
				chr(0x2800 + int(lines[i][ x : x + 2], base=16))
				for x in range(0, len(lines[i]), 2)
			]
			scene.append(line)
		return scenes

braille = BraillEngine()
