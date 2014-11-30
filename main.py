import create
import time
import Netcom
import Driver
import threading

r = create.Create(3)
r.toFullMode()

comm = Netcom.Netcom()

comm.initComms("gyumii", "oauth:i3vra1n8554xvy4ox870rnhnx10cko")

