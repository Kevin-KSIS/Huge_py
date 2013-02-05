import mechanize
import threading

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out



def check(lemail, filex):
    for email in lemail:
        try:
            if email.endswith('\n'):
                email = email[:-1]
            br = mechanize.Browser()
            br.set_handle_robots(False)
            br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
            br.open('http://www.all-nettools.com/toolbox/email-dossier.php')
            br.select_form(nr=1)
            br.form['email'] = email
            br.submit()
            if '550 Requested action not taken: mailbox unavailable' in br.response().read():
                print "Email " + email + " does not exist"
                open(filex, 'a').write(email+'\n')
            else:
                print "Email " + email + " exists"

        except:
            print "Error with " + str(email)


acs = open(raw_input("File with accounts to check: ")).readlines()
filex = raw_input("File to save working accounts into: ")
nbthreads = input("Number of threads: ")
if len(acs) > nbthreads:
    z = chunkIt(acs, nbthreads)
    for passz in z:
        threading.Thread(target=check, args=(passz, filex)).start()
else:
        z = chunkIt(acs, len(acs))
        for passz in z:
                threading.Thread(target=check, args=(passz, filex)).start()


