
class Ansi():
	# def __init__(self):
	# 	pass

	@staticmethod
	def print(ansi_code):
		print(ansi_code, end='')

	@staticmethod
	def clearScreen():
		print("\x1b[2J\x1b[H", end='')

ansi = Ansi()
