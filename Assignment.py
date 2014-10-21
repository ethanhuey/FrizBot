import create
robot = create.Create(3)
robot.toFullMode()
robot.go(100,0)

#Square
for x in range(0, 4):
        r.move(100,20)
        r.turn(90, 10)

#WallHit
while(true):
    sensors = robot.sensors([create.LEFT_BUMP, create.RIGHT_BUMP])
    if (sensors[create.LEFT_BUMP] == 1) or (sensors[create.RIGHT_BUMP] == 1):
        robot.stop()
