#lol harvester
import mechanize, re
import threading


def createbrowser():
    print "created a browser"
    br = mechanize.Browser()
    br.set_handle_gzip(True)
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1 like Mac OS X; en-US) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3')]
    return br

def harvest(link,wherefrom,whereto):
    br = createbrowser()
    print "started!!!"
    for trad in range(wherefrom,whereto):
        if trad==1:
            br.open(link)
            print trad
        else:
            print trad
            br.open(link+"&page="+str(trad))
        normalusers = re.findall("<big><font color=\"red\">([A-Z]*[a-z]*[0-9]*[A-Z]*[0-9]*[a-z]*[A-Z]*)",br.response().read())
        print normalusers
        poster = re.findall("<big>([A-Z]*[a-z]*[0-9]*[A-Z]*[0-9]*[a-z]*[A-Z]*)",br.response().read())
        print poster
        for user in normalusers:
            if user not in open("lolusers.txt",'r').read():
                open("lolusers.txt",'a').write(user+"\n")
                print user
        for user in poster:
            if user not in open("lolusers.txt",'r').read():
                open("lolusers.txt",'a').write(user+"\n")
                print user

def menu():
    link = raw_input("Enter the lol thread:\n=> ")
    whereto = input("Enter where the threads ends:\n=> ")
    factor = whereto/6
    threading.Thread(target=harvest, args=(link,1,factor*1)).start()
    threading.Thread(target=harvest, args=(link,factor*1,factor*2)).start()
    threading.Thread(target=harvest, args=(link,factor*2,factor*3)).start()
    threading.Thread(target=harvest, args=(link,factor*3,factor*4)).start()
    threading.Thread(target=harvest, args=(link,factor*4,factor*5)).start()
    threading.Thread(target=harvest, args=(link,factor*5,whereto)).start()
menu()

