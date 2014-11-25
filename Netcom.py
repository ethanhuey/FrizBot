import socket
import sys

class Netcom:
        s = None
        def initComms(self, username, password):
                #connect to chat server
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(None)
                        print("Trying irc.twitch.tv...")
                        s.connect(("irc.twitch.tv", 6667))
                        print("Connected to irc.twitch.tv")
                except:
                        sys.exit("Failed to connect")
                #send login credentials
                try:
                        s.sendall(b'PASS %s\n' %password)
                        s.sendall(b'NICK %s\n' %username)
                        #self.receive(s)
                except:
                        sys.exit("Login failed")
                #join FrizBot chatroom
                s.send(b'JOIN #frizbot8\n')
                # self.receive(s)
                print (s.recv(1024))
                
                #do nothing for now
                closeComms()
		
        def closeComms(self):
                s.close

        def receive(self, s):
                data = s.recv(4096)
                """
                data_received = 0
                while True:
                        currentblock = s.recv(min(socket.CMSG_LEN(4096) - data_received, 4096))
                        if currentblock == "":
                                break
                        data += currentblock
                        data_received += len(currentblock)
                """
                print (data)
                
