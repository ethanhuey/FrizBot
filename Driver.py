


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
				if(current == "sing")
					robot.playSong( [(88,8),(88,16),(88,16),(84,8),(88,16),(91,32),(79,16)] )
	
			else:
				commands.append("sing")
				

class Keeper:
	timer = 20;
	def keepsafe(robot):
		while True:
			sensors = robot.sensors([create.LEFT_BUMP, create.RIGHT_BUMP, create.CLIFF_FRONT_LEFT, create.CLIFF_FRONT_RIGHT, create.CLIFF_RIGHT, create.CLIFF_LEFT])
			if (sensors[create.LEFT_BUMP] == 1) or (sensors[create.RIGHT_BUMP] == 1) or (sensors[create.CLIFF_FRONT_LEFT] == 1) or (sensors[create.CLIFF_FRONT_RIGHT] == 1) or (sensors[create.CLIFF_RIGHT] == 1) or (sensors[create.CLIFF_LEFT] == 1):
				robot.stop()
				timer = 20;
			elif (timer == 0):
				robot.stop()
				timer = 20;
			else:
				timer--;


