import os
import md5
import re


def crackme():
    crackcrackme()

def crackcrackme():
    crackcrackcrackme()

def crackcrackcrackme():
    userHWID = '34e54db73e1e0b74ec430d666d204b07'
    if "Wow6432Node" in os.popen('REG QUERY HKEY_LOCAL_MACHINE\\SOFTWARE\\').read():
        HWID = md5.md5(os.popen('REG QUERY HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Cryptography\Protect\Providers /v Preferred').read().split(" ")[-1: ][0].split("\n")[0]+"VENAMTEAM").hexdigest()
    else:
        HWID = md5.md5(re.findall('MachineGuid\\.*(.*)\n' , os.popen('REG QUERY HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography /v MachineGuid').read())[0].split('\t')[-1:][0]+"VENAMTEAM").hexdigest()

    if userHWID == HWID:
        print "you are connected to the program cause you paid for it"
    else:
        print "You have no rights to use this program!!!"
        exit(0)







