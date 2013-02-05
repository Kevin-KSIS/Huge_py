import subprocess, re

myfile = open("pkglist",'r').readlines()

for a in myfile:
    try:
        pkg = re.findall("Description    : (.*)\n" , subprocess.check_output(['pacman','-Qi',a.replace("\n","")]))[0]
        open("manfiles",'a').write(pkg+"\n\n")
    except:
        pass
