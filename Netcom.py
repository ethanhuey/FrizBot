import socket
import sys

class Netcom:
	s = None
	def initComms(self, username, password):
		#connect to chat server
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect(("irc.twitch.tv", 6667))
			receive(s)
		except:
			print ("Failed to connect")
			sys.exit
		#send login credentials
		try: #not sure if try catch works here
			s.send('NICK %s\n' %username)
			s.send('PASS %s\n' %password)
			receive(s)
		except:
			print ("Login Failed")
			sys.exit
		#join FrizBot chatroom
		s.send('JOIN #frizbot\n')
		receive(s)
		
		#do nothing for now
		closeComms()
		
	def closeComms():
		s.close
	
	def receive(s):
                while True:
                        data += s.recv(2048);
                        if data == "":
                                break
                print (data)
