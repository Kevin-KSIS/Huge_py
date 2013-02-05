import mechanize
from threading import Thread


def chunkIt(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0
  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg
  return out

def checkproxy(proxy, ip):
    try:
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0')]
   
        br.set_proxies({"http": proxy})
        br.open('http://automation.whatismyip.com/n09230945.asp', timeout=10)
        if br.response().read() == proxy.split(':')[0]:
            return True
        print "Not a real proxy"
        return False
    except Exception, e:
        print e
        return False

def mainchecker(proxies, ip):
    for i in proxies:
        check = checkproxy(i, ip)
        if check:
            open('workingproxies.txt', 'a').write(i+'\n')
            print "Found {0} working".format(i)
        else:
            print "Proxy {0} is not working".format(i)
            

def main():
    ip = raw_input("Your ip address: ")
    proxies = open(raw_input("File with proxies: "), 'r').read().split('\n')
    proxies = chunkIt(proxies, 10)
    for a in proxies:
        Thread(target=mainchecker, args=(a, ip)).start()
    while 1:
        pass

main()
