#! /usr/bin/env python
# Filename: PyScan.py

import sys, socket, wx, os
from wx.lib.pubsub import Publisher
from threading import Thread

__version__ = '1.0'
__author__ = "Ki113d"
__maintainer__ = "Ki113d"
__email__ = "ki113d.69@gmail.com"
__status__ = "Development"

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(365, 365), style=wx.CAPTION | wx.SYSTEM_MENU | wx.CLOSE_BOX)
        self.panel = wx.Panel(self, -1)
        self.sizerOne = wx.BoxSizer(wx.HORIZONTAL)
        self.font = wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL)
        self.portGroup = wx.StaticBox(self.panel, -1, "Ports", (175,0), size=(170,80))
        self.portGroup.SetFont(self.font)
        self.labelIP = wx.StaticText(self.panel, -1, "IP:", (15,20))
        self.labelIP.SetFont(self.font)
        self.labelFrom = wx.StaticText(self.panel, -1, "From:", (190,20))
        self.labelFrom.SetFont(self.font)
        self.labelTo = wx.StaticText(self.panel, -1, "To:", (190,50))
        self.labelTo.SetFont(self.font)
        self.labelInfo = wx.StaticText(self.panel, -1, "Port Info:", (15,80))
        self.labelInfo.SetFont(self.font)
        self.textBoxIP = wx.TextCtrl(self.panel, 1, pos=(45,20), size=(110,20))
        self.textBoxPortFrom = wx.TextCtrl(self.panel, 2, pos=(230,20), size=(90,20))
        self.textBoxPortTo = wx.TextCtrl(self.panel, 3, pos=(230,50), size=(90,20))
        self.portList = wx.ListBox(self.panel, 4, (15,100), (330,200))
        self.aboutButton = wx.Button(self.panel, 5, "About", (15,305))
        self.scanButton = wx.Button(self.panel, 6, "Scan", (270,305))
        self.Bind(wx.EVT_BUTTON, self.onAboutPressed, id= 5)
        self.Bind(wx.EVT_BUTTON, self.onScanPressed, id=6)
        Publisher().subscribe(self.updateList, "update")
        Publisher().subscribe(self.onProgress, "scanThread")
        self.Show(True)
        
    def onAboutPressed(self, evt):
        info = wx.AboutDialogInfo()
        info.SetName('PyScan')
        info.SetVersion(__version__)
        info.SetDescription("\nPyScan is a port scanner written in python\nusing the wxpython library.\nThis tool was written for educational purposes")
        info.SetCopyright('(C) 2011 Ki113d')
        info.AddDeveloper(__maintainer__)
        wx.AboutBox(info)
        
    def onScanPressed(self, evt):
        self.portList.Clear()
        address = self.textBoxIP.GetValue()
        if len(address) < 5:
            wx.MessageBox("Please enter a valid IP address or hostname.", "Attention")
            return
        try:
            portFrom = int(self.textBoxPortFrom.GetValue())
            portTo = int(self.textBoxPortTo.GetValue())
        except ValueError as ex:
            if "invalid literal for int() with base 10: ''" in ex:
                portTo = -1
            else:
                wx.MessageBox("Ports can only be integers between 1 and 25565", "Attention")
                return
        try:
            if portFrom < 0 or portFrom > 25565:
                wx.MessageBox("Ports can only be integers between 1 and 25565", "Attention")
                return
            elif portTo < -1 or portTo == 0 or portTo > 25565:
                wx.MessageBox("Ports can only be integers between 1 and 25565", "Attention")
                return
            elif portFrom > portTo and not portTo == -1:
                wx.MessageBox("Port to can not be larger in value then port from", "Attention")
                return
        except UnboundLocalError:
            wx.MessageBox("Please enter a valid port number!", "Attention")
            return
        ScanThread(address, portFrom, portTo)

    def onProgress(self, status):
        if status.data == "started":
            self.scanButton.Disable()
        elif status.data == "finished":
            self.scanButton.Enable()
            
    def updateList(self, result):
        try:
            if isinstance(result.data[1], bool):
                if result.data[1]:
                    self.portList.AppendAndEnsureVisible("{0:<8}{1}".format(result.data[0], "Open"))
                else:
                    self.portList.AppendAndEnsureVisible("{0:<8}{1}".format(result.data[0] , "Closed"))
            elif isinstance(result.data[1], str):
                wx.MessageBox(result.data[1], "Attention")
        except wx.PyDeadObjectError:
            sys.exit(0)

    def onExit(self,e):
         self.Close(True)
         
def readReply(ip, port, reply):
    if reply[0]:
        print "{0}:{1:<10}Open".format(ip, port)
    else:
        if "getaddrinfo failed" in reply[1]:
            print "[Errno 11004] Failed to retrieve address information."
            print "Please check the ip address or hostname and try again."
            sys.exit(0)
        print "{0}:{1:<10}Closed".format(ip, port)

class ScanThread(Thread):
    def __init__(self, ip, portFrom, portTo):
        Thread.__init__(self)
        self.IP = ip
        self.portFrom = portFrom
        self.portTo = portTo
        Publisher.sendMessage("scanThread", "started")
        self.start()
        
    def run(self):
        if self.portTo == -1:
            res = self.scan(self.portFrom)
            Publisher().sendMessage("update", (self.portFrom, res))
            return 0
        else:
            for i in range(self.portFrom, self.portTo+1):
                res = self.scan(i)
                Publisher.sendMessage("update", (i, res))
        self.closing()
                
    def scan(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            sock.connect((self.IP, int(port)))
            return True
        except ValueError:
            return "Invalid port number\\s."
        except Exception as ex:
            sock.close()
            if "getaddrinfo failed" in ex:
                return "IP address/hostname seems to be incorrect, please check it and try again."
            elif "timed out" in ex:
                return False
                
    def closing(self):
        Publisher.sendMessage("scanThread", "finished")
            
def regularScan(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((ip, port))
        return (True, "")
    except Exception as ex:
        sock.close()
        return (False, ex)

if __name__ == '__main__':
    ip = ''
    port = ''
    gui = False
    if len(sys.argv) > 1:
        i = 1
        while i < len(sys.argv):
            if sys.argv[i] == '-ip':
                ip = sys.argv[i + 1]
            if sys.argv[i] == '-port':
                try:
                    port = int(sys.argv[i + 1])
                except ValueError:
                    print 'Please specify a valid port number.'
                    sys.exit(0)
            if sys.argv[i] == '-ports':            
                try:
                    lis = sys.argv[i + 1].split('-')
                    port = (int(lis[0]), int(lis[1]))
                except ValueError:
                    print 'Please specify valid port numbers.'
                    sys.exit(0)
            if sys.argv[i] == '-g':
                gui = True
            if sys.argv[i] == '-h' or sys.argv[i] == '--help':
                print "PyScan vs {0}".format(__version__)
                print "Usage: pyscan -ip www.google.com -ports 70-90"
                print " Available command line arguments:"
                print "   -ip    <ip address/hostname>  Address to scan."
                print "   -ports <portFrom>-<portTo>    Port range to scan."
                print "   -port  <port>                 Single port to scan."
                print "   -g                            Open program with GUI."
                print "   -h                            Shows this message."
                sys.exit(0)
            i += 1
    else:
        print "Please specify an IP/hostname and port."
        sys.exit(0)

    if gui:
        app = wx.App(False)
        window = MainWindow(None, "PyScan")
        app.MainLoop()
    elif ip and port:
        if isinstance(port, int):
            open = regularScan(ip, port)
            readReply(ip, port, open)
        else:
            if len(port) == 2:
                if isinstance(port[0], int) and isinstance(port[1], int):
                    if port[0] > port[1]:
                        print "Please select a valid port range to scan!"
                        sys.exit(0)
                    elif port[0] < 1 or port[0] > 25565:
                        print "Ports may only range between 1 and 25565."
                        sys.exit(0)
                    for i in range(port[0], port[1] + 1):
                        res = regularScan(ip, i)
                        readReply(ip, i, res)
    else:
        print "Please specify an IP/hostname and port."
        sys.exit(0)
