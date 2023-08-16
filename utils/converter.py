import cv2

class Braille():
	def __init__(
			self,
			braille_base = 0x2800,
			braille_len_x = 2,
			braille_len_y = 4):
		self.braille_base = braille_base
		self.braille_len_x = braille_len_x
		self.braille_len_y = braille_len_y

	def	getSect(self, board, base):
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
		self.converted.append(chr(self.braille_base + tmp_char))

	def fromBoard(self, board):
		len_y = len(board)
		len_x = len(board[0])
		self.converted = []
		for y in (range(int(len_y / self.braille_len_y))):
			for x in (range(int(len_x / self.braille_len_x))):
				self.getSect(board, (y * self.braille_len_y, x * self.braille_len_x))
			self.converted.append('\n')
		return self.converted

	def printBoard(self, board):
		board = self.fromBoard(board)
		print(''.join(board))

	def fromImg(self, path):
		# load the input image
		img = cv2.imread(path)

		# convert the input image to grayscale
		img_data = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		# apply thresholding to convert grayscale to binary image
		board = cv2.threshold(img_data,127,255,cv2.THRESH_BINARY)[1]
		# board = cv2.threshold(img_data,0,127,cv2.THRESH_BINARY)[1]
		self.printBoard(board)

braille = Braille()
