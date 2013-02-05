import urllib, re
import socket
import threading


def chunkIt(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0
  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg
  return out

def menu(list, question):
    for a in list:
        print str((list.index(a))+1) + "." + a
    print
    returned = input(question)
    return returned


class proxygrabber:
    def __init__(self):
        self.sites = ['http://elite-proxies.blogspot.com/', 'http://www.proxies.cz.cc/',
        'http://www.proxylists.net/http.txt', 'http://www.proxylists.net/http_highanon.txt',
        'http://multiproxy.org/txt_all/proxy.txt',
        'http://www.digitalcybersoft.com/ProxyList/fresh-proxy-list.shtml',
        'http://tools.rosinstrument.com/proxy/?rule1', 'http://www.scrapeboxproxies.cz.cc/',
        'http://proxylist.j1f.net/',
        'http://www.proxy-server.info/proxy-server-list.shtml',
        'http://www.proxyserverprivacy.com/free-proxy-list.shtml']

    def proxyCheck(self, proxy):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(15)
            x = proxy.split(":")
            sock.connect((x[0],int(x[1])))
            sock.settimeout(None)
            sock.close()
            return True
        except Exception, err:
            return False

    def getproxies(self):
        listx = []
        for site in self.sites:
            try:
                print "Getting proxies on " + site
                content = urllib.urlopen(site).read()
                e = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+", content)
                listx.append(e)
            except:
                pass
        return listx

    def printprox(self, listx, filex):
        listop = []
        for x in listx:
            for a in x:
              if not a in listop:
                  listop.append(a)
                  with open(filex, 'a') as f:
                    f.write(str(a)+'\n')



    def filterproxies(self, proxies):
        listp = []
        for zx in proxies:
            for prox in zx:
                if not prox in listp:
                    listp.append(prox)
        return listp

    def testproxies(self, filex, proxies):
        for proxy in proxies:
            isworking = self.proxyCheck(proxy)
            if isworking:
                fileop = open(filex, 'a')
                fileop.write(proxy+'\n')
                fileop.close()
                print "Working Proxy : " + proxy
            else:
                print proxy + " does not work"




while 1:
    listmenu = ["Grab Proxies and test them.", "Test Proxies from a .txt", "Grab Proxies without testing them"]
    what = menu(listmenu, "What do you want to do: ")
    if what == 1:
        mybot = proxygrabber()
        gotproxies = mybot.getproxies()
        proxies = mybot.filterproxies(gotproxies)
        filex = raw_input("File to save proxies into: ")
        nbthreads = input('Number of threads: ')
        if len(proxies) > nbthreads:
            z = chunkIt(proxies, nbthreads)
            for passz in z:
                threading.Thread(target=mybot.testproxies, args=(filex,passz)).start()
        else:
                z = chunkIt(proxies, len(proxies))
                for passz in z:
                    threading.Thread(target=mybot.testproxies, args=(filex,passz)).start()

        while 1:
                try:
                    pass
                except:
                    break

    elif what == 2:
        mybot = proxygrabber()
        proxies = open(raw_input("file with proxies: ")).readlines()
        filex = raw_input("File to save proxies into: ")
        nbthreads = input('Number of threads: ')
        if len(proxies) > nbthreads:
            z = chunkIt(proxies, nbthreads)
            for passz in z:
                threading.Thread(target=mybot.testproxies, args=(filex,passz)).start()
        else:
                z = chunkIt(proxies, len(proxies))
                for passz in z:
                    threading.Thread(target=mybot.testproxies, args=(filex,passz)).start()

    elif what == 3:
        mybot = proxygrabber()
        proxies = mybot.getproxies()
        mybot.printprox(proxies,raw_input("File to save to: "))

        while 1:
                try:
                    pass
                except:
                    break
