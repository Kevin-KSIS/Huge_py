#!/usr/bin/python

# autowidth.py
import sqlite3
import wx
import sys
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin


conn = sqlite3.connect('MyDb.db')
c = conn.cursor()
actresses = c.execute('''SELECT * FROM users''')

class AutoWidthListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
        ListCtrlAutoWidthMixin.__init__(self)


class Database(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(380, 230))

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        panel = wx.Panel(self, -1)

        self.list = AutoWidthListCtrl(panel)
        self.list.InsertColumn(0, 'User', width=140)
        self.list.InsertColumn(1, 'Password', width=130)
        for i in actresses:
            index = self.list.InsertStringItem(sys.maxint, i[0])
            self.list.SetStringItem(index, 1, i[1])

        hbox.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(hbox)

        self.Centre()
        self.Show(True)

app = wx.App()
Database(None, -1, 'Accounts')
app.MainLoop()
