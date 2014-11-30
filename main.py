import create
import time
import Netcom
import Driver
import threading

r = create.Create(3)
r.toFullMode()

comm = Netcom.Netcom()

comm.initComms("gyumii", "oauth:tvc5odguk60rr4d92924ix5ewl6h8bq", r)
#TODO

