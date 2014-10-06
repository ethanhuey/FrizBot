import create
robot = create.Create(3)
robot.toFullMode()
robot.go(100,0)
while(1 == 1):
    sensors = robot.sensors([create.LEFT_BUMP, create.RIGHT_BUMP])
    if (sensors[create.LEFT_BUMP] == 1) or (sensors[create.RIGHT_BUMP] == 1):
        robot.stop()
