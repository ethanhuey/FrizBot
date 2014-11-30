import create
import time
import Netcom

#PORT_NUMBER = 3 
#PORT_NUMBER = "dev/tty.KeySerial1"

#r = create.Create(PORT_NUMBER);

comm = Netcom.Netcom()
comm.initComms("gyumii", "oauth:tvc5odguk60rr4d92924ix5ewl6h8bq")
#TODO
