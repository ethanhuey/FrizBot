# a couple of key issues here
# 1. threads are necessary for all sections of the project, however my implementation leaves a lot to be desired. IE it doesnt work
# 2. someone needs to actually program in the sing command

import create
import threading
import time

thread1 = None


robot = create.Create(3)
robot.toFullMode()
commands = ["left", "forward", "forward", "right"]

def process():
	while True:
		if(len(commands) != 0):
			current = commands.pop(0)
			if(current == "left"):
				robot.turn(90, 45)
				robot.go(20,0)
			if(current == "forward"):
				robot.go(20,0)
			if(current == "right"):
				robot.turn(-90, 45)
				robot.go(20,0)

		else:
			commands.append("sing")


def keepsafe():
	while True:
		sensors = robot.sensors([create.LEFT_BUMP, create.RIGHT_BUMP, create.CLIFF_FRONT_LEFT, create.CLIFF_FRONT_RIGHT, create.CLIFF_RIGHT, create.CLIFF_LEFT])
		if (sensors[create.LEFT_BUMP] == 1) or (sensors[create.RIGHT_BUMP] == 1) or (sensors[create.CLIFF_FRONT_LEFT] == 1) or (sensors[create.CLIFF_FRONT_RIGHT] == 1) or (sensors[create.CLIFF_RIGHT] == 1) or (sensors[create.CLIFF_LEFT] == 1):
			robot.stop()

try:
	thread1 = threading.Thread(None, process(), "Thread_1", (), {}) 
	thread1.start()
	thread2 = threading.Thread(None, keepsafe(), "Thread_2", (), {}) 
	thread2.start()
except:
	print ("dang")
