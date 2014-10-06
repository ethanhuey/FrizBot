robot = create.Create(4)
sensors = robot.sensors([create.LEFT_BUMP, create.RIGHT_BUMP])
robot.toFullMode()
robot.go(100,0)
while(true):
	if (sensors[create.LEFT_BUMP] > 0 or [create.RIGHT_BUMP] > 0):
		robot.stop()