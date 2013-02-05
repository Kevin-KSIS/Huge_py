'''MADE BY VENAM'''
import wx
from mechanize import Browser
from wx.lib.anchors import LayoutAnchors
from wx.lib.pubsub import Publisher
import datetime
import mechanize
import threading
import random
import os , glob, commands, re
from cStringIO import StringIO
import time


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



##############Begining of class Hotmail Account Creator###################
class HAC(threading.Thread):

    def __init__(self, id, emaillist, myfile,trader,usingpasslist,passlist,usingaltemails,alteremaillist,capuser="",cappass=""):
        self.id = id
        self.emaillist = emaillist
        self.myfile = myfile
        self.running = False
        self.trader = trader
        self.capuser = capuser
        self.cappwd = cappass
        self.capapi = '689a8ba9bc82635447955348dbc20b25'
        self.captchaID = self.randompass()
        self.usingpasslist = usingpasslist
        self.passlist = passlist
        self.captcha2 = False
        self.usingaltemails = usingaltemails
        self.alteremaillist = alteremaillist
        threading.Thread.__init__(self)

    def setcvalue(self,captcha):
        self.captcha2 = captcha

    #generate random password
    def randompass(self):
        password=""
        for i in xrange(11):
            password+=random.choice('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW')
        return password

    #generate random name/lastname
    def randomname(self):
        naming=""
        mynoomber = random.randint(5,11)
        for i in xrange(mynoomber):
            if i%2==0 :
                if random.randint(0,4)==0:
                    naming+=random.choice(['ch',
                    'sh','ph','th','pr','ck','sr','zw','tr','kr','pl','kl','sc','dr'])
                else:
                    naming+=random.choice('bcdfghjklmnpqrstvwxyz')

            else:
                naming+=random.choice('aeiou')
        return naming

    #generate a browser
    def createbrowser(self):
        br = Browser()
        br.set_handle_gzip(True)
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1 like Mac OS X; en-US) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3')]
        return br

    #get the captcha response
    def getcaptcha(self,br):
        self.captcha2 = False
        image_response = re.findall('<img src=\"(.*)\" border=\"0\"',br.response().read())[1]
        image_response = br.open_novisit(image_response)
        image = image_response.read()
        if not self.trader:
            writing = open("captcha.gif", 'wb')
        else:
            writing = open(self.captchaID+'.gif', 'wb')
        writing.write(image)
        writing.close()
        if not self.trader:
            wx.MutexGuiEnter()
            Publisher().sendMessage("captcha", None)
            wx.MutexGuiLeave()
            while not self.captcha2:
                time.sleep(1)
            return self.captcha2
        else:
            br3 = mechanize.Browser()
            br3.open('http://www.captchatrader.com/documentation/manual_submit/file')
            br3.select_form(nr=1)
            br3.form['username'] = self.capuser
            br3.form['password'] = self.cappwd
            br3.form['api_key'] = self.capapi
            picturew = os.getcwd() + '/'+self.captchaID+'.gif'
            br3.form.add_file(open(picturew), 'text/plain', picturew, name='value')
            br3.submit()
            captcha = re.findall(re.compile('"(.*)"'), br3.response().read())[0]
            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  captcha)
            wx.MutexGuiLeave()
        return captcha

    #fill all the forms
    def fillinform(self,email):
        try:
            if self.usingpasslist == False:
                self.password = self.randompass()
            else:
                self.password = random.choice(open(self.passlist).read().split("\n"))
            if self.usingaltemails == False:
                self.resetmail = self.randompass()+"@hotmail.com"
            else:
                self.resetmail = random.choice(open(self.alteremaillist).read().split("\n"))
            self.firstname = self.randomname()
            self.lastname = self.randomname()
            self.datebirth = str(random.randint(1960,1993))
            self.br = self.createbrowser()

            ############################################

            self.br.open("https://mid.live.com/reg/reg.aspx?prp=wa%3dwsignin1.0%26id%3d258174%26wp%3dMBI_MOBILE%26wreply%3dhttps%253a%252f%252fmaccount.live.com%252f%253flc%253d1033%26lc%3d"+self.mydomainID)
            ############################################

            self.captcha = self.getcaptcha(self.br)
            self.br.select_form(nr=0)
            self.br.form['SigninNameTextBox']= email
            self.br.form['DomainList']= ['0']
            ##############################################

            self.br.form['PasswordControl$PasswordTextBox']= self.password
            self.br.form['PasswordControl$RetypePWDTextBox']= self.password
            self.br.form['AlternateEmailTextBox']= self.resetmail
            self.br.form['FirstNameTextBox']= self.firstname
            self.br.form['LastNameTextBox']= self.lastname
            self.br.form['BirthYearTextBox']= self.datebirth
            self.br.form['HIPControl$HIPSolutionTextBox']= self.captcha
            self.br.submit(name="SubmitCmd")
        except Exception,e:
            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  e)
            wx.MutexGuiLeave()
            self.fillinform(email)


    #main run function
    def run(self):
        for email in self.emaillist:
            while email.endswith("\n"):
                email = email[:-1]
            while email.endswith("\r"):
                email = email[:-1]
            email = email.lower()
            email=email.split('@')

            #get the right number
            domainlist={'live.com':'1250','hotmail.com':'10','windowslive.com':'1025','livemail.tw':'1028','live.dk':'1030','live.de':'1031','live.fi':'1035','live.fr':'1036','live.it':'1040','live.jp':'1041','live.co.kr':'1042','live.nl':'1043','live.no':'1044','live.ru':'1049','live.se':'1053','live.cn':'2052','live.co.uk':'2057','live.com.mx':'2058','live.be':'2060','live.com.pt':'2070','live.co.za':'1074','live.hk':'3076','live.at':'3079','live.com.au':'3081','live.in':'1081','live.ca':'3084','live.com.my':'1086','live.ie':'2108','live.com.ph':'1124','live.cl':'1146'}
            for domain in domainlist:
                if domain == email[1]:
                    self.mydomainID = domainlist[domain]

            #fill and submit
            self.fillinform(email[0])

            #THE ERRORS
            if "or enter a different ID" in self.br.response().read():
                wx.MutexGuiEnter()
                Publisher().sendMessage("update",  "enter a different ID")
                wx.MutexGuiLeave()
                continue
            while "characters didn't match" in self.br.response().read():
                wx.MutexGuiEnter()
                Publisher().sendMessage("update",  "Characters didn't match!")
                wx.MutexGuiLeave()
                self.fillinform(email[0])
            while "NotificationContainerError" in self.br.response().read():
                wx.MutexGuiEnter()
                Publisher().sendMessage("update",  "something is typed wrong")
                wx.MutexGuiLeave()
                self.fillinform(email[0])
            while "you can't sign up right now" in self.br.response().read():
                wx.MutexGuiEnter()
                Publisher().sendMessage("update",  "you can't sign up right now")
                wx.MutexGuiLeave()
                self.fillinform(email[0])

            #SAVE everything
            open(self.myfile,'a').write(email[0] +"@"+ email[1] + ":" + self.password + "\n")
            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "Account {"+email[0]+"@" +email[1] + "} Created with password " +self.password)
            wx.MutexGuiLeave()

        wx.MutexGuiEnter()
        Publisher().sendMessage("update",  "Finished Thread Number "+str(self.id+1))
        wx.MutexGuiLeave()

##############End of class hotmail account creator ##########################




##################################create for GUI########################
def create(parent):
    return Frame(parent)

[wxID_FRAME, wxID_FRAMEABOUTBUTTON, wxID_FRAMEALTERNATIVEBUTTON,
 wxID_FRAMEBUTTON3, wxID_FRAMECAPTCHALABEL, wxID_FRAMECHECKBOX1,
 wxID_FRAMECHECKBOX2, wxID_FRAMECHECKBOX3, wxID_FRAMEEMAILLISTLABEL,
 wxID_FRAMEEMAILLOCATIONBUTTON, wxID_FRAMEHOTCREATORLABEL,
 wxID_FRAMEINFOLABEL, wxID_FRAMELISTBOX1, wxID_FRAMENBTHREADLABEL,
 wxID_FRAMEPANEL, wxID_FRAMEPASSLISTBUTTON, wxID_FRAMESPINCTRL1,
 wxID_FRAMESTARTBUTTON, wxID_FRAMESTATICBITMAP1, wxID_FRAMETEXTCTRL1,
 wxID_FRAMETEXTCTRL2, wxID_FRAMETEXTCTRL3, wxID_FRAMETEXTCTRL4,
 wxID_FRAMEWHERETOSAVELABEL,
] = [wx.NewId() for _init_ctrls in range(24)]
#########################################################################



#########################begining of class of GUI######################
class Frame(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME, name=u'Frame', parent=prnt,
              pos=wx.Point(376, 178), size=wx.Size(801, 400),
              style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER| wx.NO_FULL_REPAINT_ON_RESIZE,
              title=u"VenamTeam's Hotmail Account Creator")
        self.SetClientSize(wx.Size(801, 400))

        self.panel = wx.Panel(id=wxID_FRAMEPANEL, name=u'panel', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(801, 400),
              style=wx.TAB_TRAVERSAL)
        image_file = 'background.jpg'
        bmp = wx.Bitmap(image_file)
        ##FOR THE BG : (I changed the parent from self.panel1 => self.bitmap)
        self.bitmap = wx.StaticBitmap(self.panel, wx.ID_ANY, bmp, (0, 0))


        self.CAPTCHAIMAGE = wx.StaticBitmap(id=wxID_FRAMESTATICBITMAP1, name='staticBitmap1',
              parent=self.panel, pos=wx.Point(640, 64), size=wx.Size(160, 97),
              style=0)

        self.spinCtrl1 = wx.SpinCtrl(id=wxID_FRAMESPINCTRL1, initial=1, max=100,
              min=1, name='spinCtrl1', parent=self.panel, pos=wx.Point(173,
              248), size=wx.Size(54, 22), style=wx.SP_ARROW_KEYS)

        self.listboxforINFOS = wx.ListBox(choices=[], id=wxID_FRAMELISTBOX1,
              name='listBox1', parent=self.panel, pos=wx.Point(308, 66),
              size=wx.Size(320, 270), style=0)



        ###LABELS###
        self.HOTCREATORLABEL = wx.StaticText(id=wxID_FRAMEHOTCREATORLABEL,
              label=u'Hotmail Account creator - VenamTeam',
              name=u'HOTCREATORLABEL', parent=self.panel, pos=wx.Point(224, 6),
              size=wx.Size(334, 21), style=0)
        self.HOTCREATORLABEL.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Verdana'))
        self.HOTCREATORLABEL.SetForegroundColour((255,255,255))
        self.HOTCREATORLABEL.SetBackgroundColour((255,255,255))

        self.EMAILLISTLABEL = wx.StaticText(id=wxID_FRAMEEMAILLISTLABEL,
              label=u'List of Emails to create : ', name=u'EMAILLISTLABEL',
              parent=self.panel, pos=wx.Point(14, 43), size=wx.Size(170, 16),
              style=0)
        self.EMAILLISTLABEL.SetForegroundColour((255,255,255))
        self.EMAILLISTLABEL.SetBackgroundColour((255,255,255))

        self.INFOLABEL = wx.StaticText(id=wxID_FRAMEINFOLABEL,
              label=u'Infos : ', name=u'INFOLABEL', parent=self.panel,
              pos=wx.Point(421, 43), size=wx.Size(50, 16), style=0)
        self.INFOLABEL.SetForegroundColour((255,255,255))
        self.INFOLABEL.SetBackgroundColour((255,255,255))

        self.WHERETOSAVELABEL = wx.StaticText(id=wxID_FRAMEWHERETOSAVELABEL,
              label=u'Where you want to save the accounts : ',
              name=u'WHERETOSAVELABEL', parent=self.panel, pos=wx.Point(13,
              183), size=wx.Size(274, 16), style=0)
        self.WHERETOSAVELABEL.SetForegroundColour((255,255,255))
        self.WHERETOSAVELABEL.SetBackgroundColour((255,255,255))

        self.NBTHREADLABEL = wx.StaticText(id=wxID_FRAMENBTHREADLABEL,
              label=u'Number of Threads : ', name=u'NBTHREADLABEL',
              parent=self.panel, pos=wx.Point(13, 251), size=wx.Size(142, 16),
              style=0)
        self.NBTHREADLABEL.SetForegroundColour((255,255,255))
        self.NBTHREADLABEL.SetBackgroundColour((255,255,255))

        self.CAPTCHALABEL = wx.StaticText(id=wxID_FRAMECAPTCHALABEL,
              label=u'Captchas', name=u'CAPTCHALABEL', parent=self.panel,
              pos=wx.Point(680, 39), size=wx.Size(63, 16), style=0)
        self.CAPTCHALABEL.SetForegroundColour((255,255,255))
        self.CAPTCHALABEL.SetBackgroundColour((255,255,255))
        ###END OF LABELS###

        ###txt control###
        self.textBoxCaptcha = wx.TextCtrl(id=wxID_FRAMETEXTCTRL2, name='textCtrl2',
              parent=self.panel, pos=wx.Point(638, 175), size=wx.Size(160, 22),
              style=0, value=u'')
        self.textBoxCaptcha.Disable()

        self.cappuser = wx.TextCtrl(id=wxID_FRAMETEXTCTRL3, name='textCtrl3',
              parent=self.panel, pos=wx.Point(16, 315), size=wx.Size(124, 22),
              style=0, value=u'USER')

        self.capppass = wx.TextCtrl(id=wxID_FRAMETEXTCTRL4, name='textCtrl4',
              parent=self.panel, pos=wx.Point(152, 315), size=wx.Size(128, 22),
              style=0, value=u'PASSWORD')
        ###END of txt control###

        ####the checkboxes###
        self.TRADERcheckBox = wx.CheckBox(id=wxID_FRAMECHECKBOX1,
              label=u' : Captcha Trader', name='checkBox1', parent=self.panel,
              pos=wx.Point(70, 289), size=wx.Size(154, 19), style=0)
        self.TRADERcheckBox.SetValue(False)
        self.TRADERcheckBox.SetForegroundColour((255,255,255))
        self.TRADERcheckBox.SetBackgroundColour((255,255,255))

        self.PASSLISTcheckBox = wx.CheckBox(id=wxID_FRAMECHECKBOX2,
              label=u' : Import Password List', name='checkBox2',
              parent=self.panel, pos=wx.Point(13, 71), size=wx.Size(189, 19),
              style=0)
        self.PASSLISTcheckBox.SetValue(False)
        self.PASSLISTcheckBox.SetForegroundColour((255,255,255))
        self.PASSLISTcheckBox.SetBackgroundColour((255,255,255))

        self.ALTERcheckBox = wx.CheckBox(id=wxID_FRAMECHECKBOX3,
              label=u' : Import Alternative Emails List', name='checkBox3',
              parent=self.panel, pos=wx.Point(13, 119), size=wx.Size(245, 19),
              style=0)
        self.ALTERcheckBox.SetValue(False)
        self.ALTERcheckBox.SetForegroundColour((255,255,255))
        self.ALTERcheckBox.SetBackgroundColour((255,255,255))
        ###END of checkboxes###

        ###buttons###
        self.LOCATION_TO_SAVE_TO_button = wx.Button(id=wxID_FRAMETEXTCTRL1,label=u'Location to save to', name='wheretosave',
              parent=self.panel, pos=wx.Point(42, 205), size=wx.Size(180, 28),
              style=0)
        self.LOCATION_TO_SAVE_TO_button.Bind(wx.EVT_BUTTON, self.Ontosavetobutton)

        self.ALTERNATIVEBUTTON = wx.Button(id=wxID_FRAMEALTERNATIVEBUTTON,
              label=u'Alternative Emails', name=u'ALTERNATIVEBUTTON',
              parent=self.panel, pos=wx.Point(42, 137), size=wx.Size(180, 28),
              style=0)
        self.ALTERNATIVEBUTTON.Bind(wx.EVT_BUTTON, self.Onalternativebutton)

        self.ABOUTBUTTON = wx.Button(id=wxID_FRAMEABOUTBUTTON, label=u'About',
              name=u'ABOUTBUTTON', parent=self.panel, pos=wx.Point(738, 361),
              size=wx.Size(42, 28), style=0)
        self.ABOUTBUTTON.SetFont(wx.Font(6, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Verdana'))
        #creating a button event handler
        self.ABOUTBUTTON.Bind(wx.EVT_BUTTON, self.ONaboutbutton)

        self.STARTBUTTON = wx.Button(id=wxID_FRAMESTARTBUTTON,
              label=u'Start Creating', name=u'STARTBUTTON', parent=self.panel,
              pos=wx.Point(321, 361), size=wx.Size(153, 28), style=0)
        self.STARTBUTTON.Bind(wx.EVT_BUTTON, self.ONSTART)

        self.captchaButton = wx.Button(id=wxID_FRAMEBUTTON3, label=u'Submit',
              name='button3', parent=self.panel, pos=wx.Point(647, 199),
              size=wx.Size(152, 28), style=0)
        self.captchaButton.Disable()
        self.captchaButton.Bind(wx.EVT_BUTTON, self.onCaptchaPressed)

        self.EMAILLOCATIONBUTTON = wx.Button(id=wxID_FRAMEEMAILLOCATIONBUTTON,
              label=u'Emails Location', name=u'EMAILLOCATIONBUTTON',
              parent=self.panel, pos=wx.Point(183, 39), size=wx.Size(118, 28),
              style=0)
        self.EMAILLOCATIONBUTTON.Bind(wx.EVT_BUTTON, self.Onemaillocbutton)

        self.PASSLISTBUTTON = wx.Button(id=wxID_FRAMEPASSLISTBUTTON,
              label=u'Password List Location', name=u'PASSLISTBUTTON',
              parent=self.panel, pos=wx.Point(42, 90), size=wx.Size(177, 28),
              style=0)
        self.PASSLISTBUTTON.Bind(wx.EVT_BUTTON, self.Onpasslistbutton)
        ###END of buttons###

#######################__INIT__################################
    def __init__(self, parent):
        self._init_ctrls(parent)
        Publisher().subscribe(self.getcaptcha, "captcha")
        #Handle thing going in the logs box
        Publisher().subscribe(self.updateList, "update")
        self.passlist = ""
        self.alteremaillist = ""
        self.emaillist = ""
        self.wheretosave = ""
        self.mycaptcha = ""
        self.mythreads = []
###############################################################

    def scale_bitmap(self, bitmap, width, height):
        image = wx.ImageFromBitmap(bitmap)
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.BitmapFromImage(image)
        return result

    def getcaptcha(self, evt):
        stream = StringIO(open('captcha.gif', "rb").read())
        bmp = wx.Bitmap("captcha.gif")
        bmp = self.scale_bitmap(bmp, 155, 100)
        self.CAPTCHAIMAGE.SetBitmap(bmp)
        self.captchaButton.Enable()
        self.textBoxCaptcha.Enable()

    def updateList(self, result):
        try:
            now = datetime.datetime.now()
            self.listboxforINFOS.AppendAndEnsureVisible("{0:<1}{1}".format(now.strftime("[%H:%M:%S]") , result.data))
        except wx.PyDeadObjectError:
            sys.exit(0)


    ######---Start events/actions handlers---######
    def ONaboutbutton(self,event):
        d= wx.MessageDialog( self, "This Program was coded by Venam and toki (VenamTeam)\nNote that the multithreaded option only works when using captchatrader!\nEnjoy!","Infos", wx.OK)
        #create msg wth ok button
        d.ShowModal() #show it
        d.Destroy() #destroy it when finished


    #Ontosavetobutton
    def Ontosavetobutton(self,event):
        dialog = wx.FileDialog ( None, style = wx.OPEN )
        # Show the dialog and get user input
        if dialog.ShowModal() == wx.ID_OK:
            self.WHERETOSAVELABEL.SetForegroundColour((0,226,0))
            self.WHERETOSAVELABEL.SetBackgroundColour((0,226,0))
            self.wheretosave = dialog.GetPath()
            Publisher().sendMessage("update",  "Saving to: "+self.wheretosave)
            self.Update()
        # The user did not select anything
        else:
            self.WHERETOSAVELABEL.SetForegroundColour((226,0,0))
            self.WHERETOSAVELABEL.SetBackgroundColour((226,0,0))
            self.wheretosave = ""
            Publisher().sendMessage("update",  "Saving to: "+self.wheretosave)
            self.Update()
        # Destroy the dialog
        dialog.Destroy()

    def Onemaillocbutton(self,event):
        dialog = wx.FileDialog ( None, style = wx.OPEN )
        # Show the dialog and get user input
        if dialog.ShowModal() == wx.ID_OK:
            self.EMAILLISTLABEL.SetForegroundColour((0,226,0))
            self.EMAILLISTLABEL.SetBackgroundColour((0,226,0))
            self.emaillist = dialog.GetPath()
            Publisher().sendMessage("update",  "Emails list: "+self.emaillist)
            self.Update()
        # The user did not select anything
        else:
            self.EMAILLISTLABEL.SetForegroundColour((226,0,0))
            self.EMAILLISTLABEL.SetBackgroundColour((226,0,0))
            self.emaillist = ""
            Publisher().sendMessage("update",  "Emails list: "+self.emaillist)
            self.Update()
        # Destroy the dialog
        dialog.Destroy()


    def Onalternativebutton(self,event):
        dialog = wx.FileDialog ( None, style = wx.OPEN )
        # Show the dialog and get user input
        if dialog.ShowModal() == wx.ID_OK:
            self.ALTERcheckBox.SetValue(True)
            self.ALTERcheckBox.SetForegroundColour((0,226,0))
            self.ALTERcheckBox.SetBackgroundColour((0,226,0))
            self.alteremaillist = dialog.GetPath()
            Publisher().sendMessage("update",  "Alternative emails list: "+self.alteremaillist)
            self.Update()
        # The user did not select anything
        else:
            self.ALTERcheckBox.SetValue(False)
            self.ALTERcheckBox.SetForegroundColour((226,0,0))
            self.ALTERcheckBox.SetBackgroundColour((226,0,0))
            self.alteremaillist = ""
            Publisher().sendMessage("update",  "Alternative emails list: "+self.alteremaillist)
            self.Update()
        # Destroy the dialog
        dialog.Destroy()

    def Onpasslistbutton(self,event):
        dialog = wx.FileDialog ( None, style = wx.OPEN )
        # Show the dialog and get user input
        if dialog.ShowModal() == wx.ID_OK:
            self.PASSLISTcheckBox.SetValue(True)
            self.PASSLISTcheckBox.SetForegroundColour((0,226,0))
            self.PASSLISTcheckBox.SetBackgroundColour((0,226,0))
            self.passlist = dialog.GetPath()
            Publisher().sendMessage("update",  "passlist: "+self.passlist)
            self.Update()
        # The user did not select anything
        else:
            self.PASSLISTcheckBox.SetValue(False)
            self.PASSLISTcheckBox.SetForegroundColour((226,0,0))
            self.PASSLISTcheckBox.SetBackgroundColour((226,0,0))
            self.passlist = ""
            Publisher().sendMessage("update",  "passlist: "+self.passlist)
            self.Update()
        # Destroy the dialog
        dialog.Destroy()
    def onCaptchaPressed(self,event):
        self.captchaButton.Disable()
        self.textBoxCaptcha.Disable()
        self.mycaptcha = str(self.textBoxCaptcha.GetValue())
        self.textBoxCaptcha.Value = ""
        self.mythreads[0].setcvalue(self.mycaptcha)

    def ONSTART(self,event):

        emaillist = open(self.emaillist).readlines()
        myfile = self.wheretosave
        trader = self.TRADERcheckBox.GetValue()
        capuser,cappass = self.cappuser.GetValue() , self.capppass.GetValue()
        nbthread= int(self.spinCtrl1.GetValue())
        usingpasslist = self.PASSLISTcheckBox.GetValue()
        usingaltemails = self.ALTERcheckBox.GetValue()

        if usingpasslist == False:
            self.passlist = ""
        if usingaltemails == False:
            self.alteremaillist = ""

        if trader==False:
            nbthread=1

        z = chunkIt(emaillist, nbthread)

        for i, i2 in enumerate(z):
            Mythread = HAC(i,i2,myfile,trader,usingpasslist,self.passlist,usingaltemails,self.alteremaillist,capuser,cappass)
            self.mythreads.append(Mythread)
            Mythread.start()

#######################END OF GUI CLASS##########################################

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()


'''
live.com,
hotmail.com,
windowslive.com,
livemail.tw,
live.dk,
live.de,
live.fi,
live.fr,
live.it,
live.jp,
live.co.kr,
live.nl,
live.no,
live.ru,
live.se,
live.cn,
live.co.uk,
live.com.mx,
live.be,
live.com.pt,
live.co.za,
live.hk,
live.at,
live.com.au,
live.in,
live.ca,
live.com.my,
live.ie,
live.com.ph,
live.cl
'''
