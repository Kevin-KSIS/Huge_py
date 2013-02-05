# -*- coding: utf-8 -*-
import socket,time,mechanize,cleverbot
host = 'irc.freenode.com'
port = 6667
NICK = 'God'
IDENT='The one and Only'
Channel = '#loss'
readbuffer=''
s=''
REALNAME="mabot0"


###########################################################
def Iamconnected():
    global s
    global host
    global port
    global NICK
    global IDENT
    global Channel
    global readbuffer
    global REALNAME
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send("NICK "+ NICK +"\r\n")
    s.send('USER '+IDENT+' '+host+' '+ NICK +' :'+REALNAME+'\n') #Identify to server
###########################################################



###########################################################
dico = {
'sexy':"banana slamma!",
"zizi":"Your zizi is so so big multiple views of it ┌∩┐ | c[",
"windows":"windoze??? Proprietary software are bad",
"backtrack":"Please I want the r00t password!!!",
"horny":"wanna lick it?",
"jesus":"I am raptorjesus",
"stfu":"stfu yourself",
"banana":"banana with icecream",
"help me":"Google is the answer!",
"reading":"reading is for n00b, I use telepathy",
"bash":"bash is for n00b (quote from kill3d)",
"bot":"there's not bots in this room especially me"
}
cb=cleverbot.Session()
###########################################################
def readIRC():
    while 1:
        global dico
        global s
        global host
        global port
        global NICK
        global IDENT
        global Channel
        global readbuffer


        ircmsg = s.recv(1024)
        ircmsg = ircmsg.strip('\n')
        if "\r" in ircmsg:
           ircmsg = ircmsg.strip("\r")
        ircmsg = ircmsg.lower()
        print "READING"
        if ircmsg.find("ping :") != -1:
            if ircmsg.find("timeout") != -1 or ircmsg.find("quit") != -1:
                print("beep----------------------------------")
            else:
                ping = ircmsg.split("ping :")
                s.send("PONG "+ ping[1] +"\n")
        s.send("JOIN "+ Channel +"\n")
        print ircmsg
        for a in dico:
            if a in str(ircmsg):
                s.send("PRIVMSG " + Channel + " :"+dico[a]+"\n")
        themsg = ircmsg.split(":")[-1:][0].replace("god ","").replace("god","")
        if "god" in str(ircmsg) and themsg!="":
            print themsg
            cbanswer=cb.Ask(ircmsg)
            s.send("PRIVMSG " + Channel + " :"+cbanswer.replace("Cleverbot","").replace("cleverbot","")+"\n")
        ircmsg=""
        time.sleep(3)

def main():
    try:
        Iamconnected()
        readIRC()
    except Exception,e:
        print e
        s.close()
        time.sleep(10)
        main()

###########################################################

main()
