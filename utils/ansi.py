
class Ansi():
	"""
	Class
	-----
	Helper with ansi code

	Attributes
	----------
	None

	Methods
	-------
	print(ansi_code)
		Print string without newline

	clearScreen()
		Clear the screen and move the cursor to (0,0)

	disableCursor()
		Hide cursor

	enableCursor()
		Unhide cursor
	"""
	@staticmethod
	def print(ansi_code):
		"""
		print
		-----
		Print string without newline

		Parameters
		----------
		ansi_code :
			the string to print
		"""
		print(ansi_code, end='')

	@staticmethod
	def clearScreen():
		"""
		clearScreen
		-----
		Clear the screen and move the cursor to (0,0)
		"""
		ansi.print("\x1b[2J\x1b[H")

	@staticmethod
	def enableCursor():
		"""
		enableCursor
		-----
		Unhide cursor
		"""
		ansi.print("\x1b[?25h")

	@staticmethod
	def disableCursor():
		"""
		disableCursor
		-----
		Hide cursor
		"""
		ansi.print("\x1b[?25l")

ansi = Ansi()
