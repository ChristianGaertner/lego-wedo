import time
import sys
from wedo import WeDo
from wedoCommon import stopAll

def changeMouth(wd, openIt=True):
	speed = -30
	sleepFor = 0.7

	if openIt:
		speed = -speed
		sleepFor += 0.1

	wd.motor_b = speed
	time.sleep(sleepFor)
	wd.motor_b = 0

def openMouth(wd):
	print("opening")
	changeMouth(wd, openIt=True)

def closeMouth(wd):
	print("closing")
	changeMouth(wd, openIt=False)

wd = WeDo()

openMouth(wd)

mouthIsOpen = True
run = True

closedFor = 0

blockOperationFor = 0

while True:
	print(wd.raw_distance)
	time.sleep(0.01)

while run:
	try:
		if wd.raw_distance is None:
			continue
		elif wd.raw_distance > 77:
			blockOperationFor = 0
		elif wd.raw_distance < 77 and mouthIsOpen and blockOperationFor is 0:
			closeMouth(wd)
			mouthIsOpen = False
		elif closedFor > 10:
			openMouth(wd)
			mouthIsOpen = True
			closedFor = 0
			blockOperationFor = 5

		if not mouthIsOpen:
			closedFor += 1

		if blockOperationFor > 0:
			blockOperationFor -= 1
		print(wd.raw_distance)		
		time.sleep(0.5)
	except:
		print("Unexpected error:", sys.exc_info()[0])
		run = False

stopAll(wd)