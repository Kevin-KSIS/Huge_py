import mechanize, threading, random, time
alpha = 'abcdefghijjklmnopqrstuvwxyz'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out

def checkacc(emaillist, filex):
    for email in emaillist:
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
            if 'Live ID doesn\'t exist' in br.response().read():
                    print "["+bcolors.OKGREEN + "+" + bcolors.ENDC +"]This email {"+email+"} Does not exist"
                    open(filex, 'a').write(email+'\n')
            else:
                print "["+bcolors.FAIL + "-" + bcolors.ENDC +"]This email {"+email+"} Already exist"

        except:
            print "["+bcolors.WARNING + "~" + bcolors.ENDC +"]Error with {"+email+"}"
            open(Errorlogs, 'a').write(email+'\n')
        br.close()



def menuhotmailchecker():
    print bcolors.OKGREEN +"\n                                                                 _     \n _____ _          _____                      _____              | |    \n|_   _| |_ ___   |  |  |___ ___ ___ _____   |_   _|___ ___ _____|_|___ \n  | | |   | -_|  |  |  | -_|   | .'|     |    | | | -_| .'|     | |_ -|\n  |_| |_|_|___|   \___/|___|_|_|__,|_|_|_|    |_| |___|__,|_|_|_| |___|"
    print "  _   _   _   _   _   _   _     _   _   _   _   _   _   _  \n / \ / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ \n( "+bcolors.FAIL+"H"+bcolors.OKGREEN+" | "+bcolors.FAIL+"o"+bcolors.OKGREEN+" | "+bcolors.FAIL+"t"+bcolors.OKGREEN+" | "+bcolors.FAIL+"m"+bcolors.OKGREEN+" | "+bcolors.FAIL+"a"+bcolors.OKGREEN+" | "+bcolors.FAIL+"i"+bcolors.OKGREEN+" | "+bcolors.FAIL+"l"+bcolors.OKGREEN+" ) ( "+bcolors.FAIL+"C"+bcolors.OKGREEN+" | "+bcolors.FAIL+"h"+bcolors.OKGREEN+" | "+bcolors.FAIL+"e"+bcolors.OKGREEN+" | "+bcolors.FAIL+"c"+bcolors.OKGREEN+" | "+bcolors.FAIL+"k"+bcolors.OKGREEN+" | "+bcolors.FAIL+"e"+bcolors.OKGREEN+" | "+bcolors.FAIL+"r"+bcolors.OKGREEN+" )\n \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \n"+bcolors.ENDC

    emaillist = open(raw_input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]Location Of the Emails\n=> ")).readlines()
    filex = raw_input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]Location to Save Emails to\n=> ")
    nbthreads = input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]How many Threads will be working at the same time?\n=> ")
    if len(emaillist) >= nbthreads:
        z = chunkIt(emaillist, nbthreads)
        for passz in z:
            threading.Thread(target=checkacc, args=(passz, filex)).start()
    else:
        z = chunkIt(emaillist, len(emaillist))
        for passz in z:
            threading.Thread(target=checkacc, args=(passz, filex)).start()


menuhotmailchecker()


