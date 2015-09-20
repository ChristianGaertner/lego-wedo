import time
from wedo import WeDo
from wedoCommon import stopAll

wd = WeDo()

stopAll(wd)


def move(wd, out=True):
	speed = 100
	sleepFor = 1.6
	if out:
		speed = -speed
		sleepFor -= 0.1

	wd.motor_a = speed
	time.sleep(sleepFor)
	wd.motor_a = 0

def push(wd):
	move(wd, out=False)
	move(wd, out=True)

while True:
	time.sleep(0.1)
	
	print(wd.raw_distance)
	if wd.raw_distance < 80:
		push(wd)