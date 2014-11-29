


class Processor:
	commands = ["left", "forward", "forward", "right"]
	def process(robot):
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
				

class Keeper:
	def keepsafe(robot):
		while True:
			sensors = robot.sensors([create.LEFT_BUMP, create.RIGHT_BUMP, create.CLIFF_FRONT_LEFT, create.CLIFF_FRONT_RIGHT, create.CLIFF_RIGHT, create.CLIFF_LEFT])
			if (sensors[create.LEFT_BUMP] == 1) or (sensors[create.RIGHT_BUMP] == 1) or (sensors[create.CLIFF_FRONT_LEFT] == 1) or (sensors[create.CLIFF_FRONT_RIGHT] == 1) or (sensors[create.CLIFF_RIGHT] == 1) or (sensors[create.CLIFF_LEFT] == 1):
				robot.stop()


