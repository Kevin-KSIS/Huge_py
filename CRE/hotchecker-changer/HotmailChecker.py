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


###########ACTUAL CHECKER #########################
def checkacc(emaillist, filex, len_acs):
    global n
    for email in emaillist:
        n+=1
        try:
            if email.endswith('\n'):
                email = email[:-1]
            br = mechanize.Browser()
            br.set_handle_robots(False)
            br.set_handle_redirect(True)
            br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
            br.open('http://login.live.com/?id=1')
            br.select_form(nr=0)
            br.form['login'] = email
            br.form['passwd'] = random.choice(alpha)*6
            br.submit()
            if 'doesn\'t exist' in br.response().read():
                    printed= "[+]This email {"+email+"} Does not exist"
                    wx.MutexGuiEnter()
                    Publisher().sendMessage("update",printed +" " + timing(n,len_acs))
                    wx.MutexGuiLeave()
                    if email not in open(filex,'r').read():
                        open(filex, 'a').write(email+'\n')
            else:
                printed= "[-]This email {"+email+"} Already exist"
                wx.MutexGuiEnter()
                Publisher().sendMessage("update",printed +" " + timing(n,len_acs))
                wx.MutexGuiLeave()

        except:
            printed= "[-]Error with {"+email+"}"
            wx.MutexGuiEnter()
            Publisher().sendMessage("update",printed +" " + timing(n,len_acs))
            wx.MutexGuiLeave()
        br.close()
##############END OF CHECKER################


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
              title=u'Hotmail Checker - VenamTeam')
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
        self.listlabel.SetBackgroundColour((21,21,21))

        self.infoslabel = wx.StaticText(id=wxID_FRAMEINFOSLABEL,
              label=u'INFOS : ', name=u'infoslabel', parent=self.panel1,
              pos=wx.Point(226, 109), size=wx.Size(58, 16), style=0)
        self.infoslabel.SetForegroundColour((255,255,255))
        self.infoslabel.SetBackgroundColour((21,21,21))

        self.titlelabel = wx.StaticText(id=wxID_FRAMETITLELABEL,
              label=u'Hotmail Checker - VenamTeam', name=u'titlelabel',
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
        len_acs=len(emaillist)
        filex = self.wheretosave
        nbthreads = int(open("config.data.txt",'r').read())

        if len(emaillist) >= nbthreads:
            z = chunkIt(emaillist, nbthreads)
            for passz in z:
                threading.Thread(target=checkacc, args=(passz, filex,len_acs)).start()
        else:
            z = chunkIt(emaillist, len(emaillist))
            for passz in z:
                threading.Thread(target=checkacc, args=(passz, filex,len_acs)).start()
############# END OF GUI #########################


############ MAIN LOOP ################
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
