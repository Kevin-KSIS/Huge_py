#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAMEPANEL,wxID_FRAME1, wxID_FRAME1LABEL_MINECRAFT, wxID_FRAME1LISTBOX1,
 wxID_FRAME1PROXIESBUTTON, wxID_FRAME1PROXYLABEL, wxID_FRAME1SARTBUTTON,
 wxID_FRAME1STATUSLABEL, wxID_FRAME1TEXTBOXLINK,
] = [wx.NewId() for _init_ctrls in range(9)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(439, 230), size=wx.Size(674, 331),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(674, 331))
        ####need to change the parent panel to this one
        self.panel = wx.Panel(id=wxID_FRAMEPANEL, name=u'panel', parent=self,
        pos=wx.Point(0, 0), size=wx.Size(801, 400),
        style=wx.TAB_TRAVERSAL)

        image_file = 'background.jpg'
        bmp = wx.Bitmap(image_file)
        ##FOR THE BG : (I changed the parent from self.panel1 => self.bitmap)
        self.bitmap = wx.StaticBitmap(self.panel, wx.ID_ANY, bmp, (0, 0))

        self.textboxlink = wx.TextCtrl(id=wxID_FRAME1TEXTBOXLINK,
              name=u'textboxlink', parent=self.panel, pos=wx.Point(64, 36),
              size=wx.Size(560, 22), style=0, value=u'Link')

        self.Label_minecraft = wx.StaticText(id=wxID_FRAME1LABEL_MINECRAFT,
              label=u'Minecraft Servers- VenamTeam', name=u'Label_minecraft',
              parent=self.panel, pos=wx.Point(207, 8), size=wx.Size(270, 21),
              style=0)
        self.Label_minecraft.SetFont(wx.Font(13, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Verdana'))
        self.Label_minecraft.SetForegroundColour((255,255,255))
        self.Label_minecraft.SetBackgroundColour((255,255,255))

        self.Statuslabel = wx.StaticText(id=wxID_FRAME1STATUSLABEL,
              label=u'Status :', name=u'Statuslabel', parent=self.panel,
              pos=wx.Point(295, 112), size=wx.Size(56, 16), style=0)
        self.Statuslabel.SetForegroundColour((255,255,255))
        self.Statuslabel.SetBackgroundColour((255,255,255))

        self.listBox1 = wx.ListBox(choices=[], id=wxID_FRAME1LISTBOX1,
              name='listBox1', parent=self.panel, pos=wx.Point(32, 136),
              size=wx.Size(608, 144), style=0)

        self.sartbutton = wx.Button(id=wxID_FRAME1SARTBUTTON, label=u'Start',
              name=u'sartbutton', parent=self.panel, pos=wx.Point(239, 291),
              size=wx.Size(175, 28), style=0)

        self.proxiesbutton = wx.Button(id=wxID_FRAME1PROXIESBUTTON,
              label=u'Choose a proxy list', name=u'proxiesbutton', parent=self.panel,
              pos=wx.Point(192, 67), size=wx.Size(429, 28), style=0)

        self.proxylabel = wx.StaticText(id=wxID_FRAME1PROXYLABEL,
              label=u'PROXY', name=u'proxylabel', parent=self.panel, pos=wx.Point(119,
              72), size=wx.Size(45, 16), style=0)
        self.proxylabel.SetForegroundColour((255,255,255))
        self.proxylabel.SetBackgroundColour((255,255,255))

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.proxy = ""
        self.link= ""


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
