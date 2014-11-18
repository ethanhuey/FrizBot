import socket

def initComms(username, password):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("irc.twitch.tv", 6667))
    except:
        print "Failed to connect"
        return

    try:
        s.send('NICK %s\n' %username)
        s.send('PASS %s\n' %password)
    except:
        print "Login Failed"
        return

    s.send('JOIN FrizBot\n')
    s.recv(1024)
