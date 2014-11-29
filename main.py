import create
import time
import Netcom
import Driver
import threading

r = create.Create(3)
r.toFullMode()

comm = Netcom.Netcom()
proc = Driver.Processor()
keep = Driver.Keeper()

comm.initComms("gyumii", "oauth:i3vra1n8554xvy4ox870rnhnx10cko")
try:
	thread1 = threading.Thread(None, proc.process(r), "Thread_1", (), {}) 
	thread1.start()
	thread2 = threading.Thread(None, keep.keepsafe(r), "Thread_2", (), {}) 
	thread2.start()
except:
	print ("dang")
