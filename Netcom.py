import socket
import sys

class Netcom:
	s = None
	def initComms(self, username, password):
		#connect to chat server
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect(("irc.twitch.tv", 6667))
			print s.receive()
		except:
			print "Failed to connect"
			sys.exit
		#send login credentials
		try: #not sure if try catch works here
			s.send('NICK %s\n' %username)
			s.send('PASS %s\n' %password)
			print s.receive()
		except:
			print "Login Failed"
			sys.exit
		#join FrizBot chatroom
		s.send('JOIN #frizbot\n')
		print s.receive()
		
		#do nothing for now
		closeComms()
		
	def closeComms():
		s.close
	
	def receive():
		if (MSGLEN > 2048):
			data = None
			dataRcvd = 0
			while dataRcvd < MSGLEN:
				data += s.recv(min(MSGLEN-dataRcvd, 2048) #?
				if data == '':
					raise RuntimeError("connection broken")
				dataRcvd += len(data)
		else: 
			return s.recv(MSGLEN)
		
		
		
		
		
		
