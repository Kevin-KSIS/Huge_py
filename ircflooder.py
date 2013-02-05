import socket
import time
import string
import random
import socks
import socket
import sys


server = "irc.anonops.li"
port = 6667
nick = "toki22"
chn = "#Pros"

try:
    ircsock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    ircsock.connect ( (server, port) )
    ircsock.send("NICK "+ nick +"\r\n") 
    ircsock.send("USER "+ nick +" "+ nick +" "+ nick +" :"+ nick +"\r\n")
    while 1:
        ircmsg = ircsock.recv(1024)
        ircmsg = ircmsg.strip('\n')
        if "\r" in ircmsg:
           ircmsg = ircmsg.strip("\r")
        ircmsg = ircmsg.lower()
        chn = "#Programmers"
        print ircmsg
        ircsock.send("JOIN "+ chn +"\n")
        if ircmsg.find("ping :") != -1:
            if ircmsg.find("timeout") != -1 or ircmsg.find("quit") != -1:
                print("beep")
        
            else:
                ping = ircmsg.split("ping :")
                ircsock.send("PONG "+ ping[1] +"\n")
                ircsock.send("JOIN "+ chn +"\n")
        ircsock.send("PRIVMSG " + chn + " :Hello there!\n")
        time.sleep(1)

except:
    ircsock.close()
    e = sys.exc_info()[1]
    print e
    
    
