import time
import random

from utils.ansi				import ansi
from utils.braillEngine		import braille

import utils.signal

import os

TMP_DIR="./tmp"
if not os.path.isdir(TMP_DIR):
	os.mkdir(TMP_DIR)

TMP_DIR+="/"
