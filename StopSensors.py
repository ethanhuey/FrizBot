import create
robot = create.Create(3)
robot.toFullMode()
while True:
sensors = robot.sensors([create.LEFT_BUMP, create.RIGHT_BUMP, create.CLIFF_FRONT_LEFT, create.CLIFF_FRONT_RIGHT, create.CLIFF_RIGHT, create.CLIFF_LEFT])
if (sensors[create.LEFT_BUMP] == 1) or (sensors[create.RIGHT_BUMP] == 1) or (sensors[create.CLIFF_FRONT_LEFT] == 1) or (sensors[create.CLIFF_FRONT_RIGHT] == 1) or (sensors[create.CLIFF_RIGHT] == 1) or (sensors[create.CLIFF_LEFT] == 1):
robot.stop()
