import signal

def sigIntHandler(signum, frame):
	print("\x1b[?25h")
	exit(130)

signal.signal(signal.SIGINT, sigIntHandler)
print("\x1b[?25l")
