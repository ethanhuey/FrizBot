import socket
import sys
import re
import Driver

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
                        self.closeComms()
                        sys.exit("Failed to connect")
                #send login credentials
                try:
                        s.sendall(('PASS %s\n' %password).encode('utf8', 'strict'))
                        s.sendall(('NICK %s\n' %username).encode('utf8', 'strict'))
                except:
                        self.closeComms()
                        sys.exit("Login failed")
                #join FrizBot chatroom
                s.send(('JOIN #frizbot8\n').encode('utf8', 'strict'))
                print (s.recv(1024))
                proc = Driver.Processor()
                try:
                        while True:
                                message = self.receiveMessages(s)
                                proc.process(message)
                                print (message, end="")
                except KeyboardInterrupt:
                        self.closeComms()
                        sys.exit("\nKeyboard Interrupt")
        
        def closeComms(self):
                if self.s:
                        self.s.close()
        
        def receiveMessages(self, s):
                message = s.recv(1024).decode('utf8', 'strict')
                m = re.match((r'^.*:([a-zA-Z0-9]*)\![a-zA-Z0-9]*@[a-zA-Z0-9]*\.tmi\.twitch\.tv PRIVMSG #frizbot8 :(.*).*$'), message)
                
                if m:
                        return (m.group(1)+': '+m.group(2)+'\n')
                return ""
                
