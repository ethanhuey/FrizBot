
class Processor:
	def process(self, robot, current):
		if(current == "left"):
			robot.turn(90, 45)
			robot.go(20,0)
		if(current == "move"):
			robot.go(20,0)
		if(current == "right"):
			robot.turn(-90, 45)
			robot.go(20,0)
		if(current == "sing"):
			robot.playSong( [(88,8),(88,16),(88,16),(84,8),(88,16),(91,32),(79,16)] )




