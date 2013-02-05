import urllib2, urllib, socket, time, sys, os, random
from threading import Thread, active_count

"""
sys.argv:
1:pathTofile
2:linkToVisit
"""

def get(maxln):
    arry = []
    place= 0
    filehandle = open(sys.argv[1], 'r')
    while place < maxln:
        place = place + 1
        arry.append(filehandle.readline())
    return arry;


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1 # + 1, it just needs it to be accurate


def is_bad_proxy(pip):
    try:
        proxy_handler = urllib2.ProxyHandler({'http': pip})
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)
        req=urllib2.Request(sys.argv[2])  # change the URL to test here
        sock=urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        #print 'Error code: ', e.code
        return e.code
    except Exception, detail:
        #print "ERROR:", detail
        return True
    return False

def main():
    if place > maxln:
        sys.exit()
    socket.setdefaulttimeout(35) #in seconds
    global goodarray
    if is_bad_proxy(currentProxy):
        #print "Bad Proxy %s" % (currentProxy) #this does not edit the global value
        pass
    else:
        #print "Good Proxy %s" % (currentProxy)
        goodarray.append(currentProxy)

def loop():
    global goodarray
    global currentProxy #make it global
    global place
    global maxln
    proxylimit = 100 #-------------------# How many threads can be run at once!
    maxln = file_len(sys.argv[1]); #Get ammount of lines in prx.txt
    proxyList = get(maxln); #put the lines from the file into an array
    goodarray = []
    loopplace = 0
    place = 0
    while place != maxln:

        place = place + 1
        refresh = 0
        os.system("clear")
        print "Active threads: " + str(active_count()) + "/" + str(proxylimit)
        print "Done: " + str(place) + "/" + str(maxln)
        print "Good Proxies: " + str(len(goodarray))
        g = float(len(goodarray))
        pp = float(place)
        print "Percentage: " + str((g / pp)*100.000) + "%"
        #print "Good Proxies: " + "\n\n" + str(goodarray)

        time.sleep(proxylimit / 1000)
        if active_count() < proxylimit:
            #default coding <-------
            try:
                currentProxy = proxyList[loopplace];
            except:
                sys.exit()
            loopplace = loopplace + 1;
            Thread(target=main, args=()).start()
            #within here -------->

    f = open("goodprx~"+ str(random.randint(0, 100000))+".txt", 'w')
    for i in goodarray:
        f.write(i)
    f.close()

if __name__ == '__main__':
    while 1:
        loop()
