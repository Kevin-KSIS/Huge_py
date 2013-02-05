import mechanize
from threading import Thread

myip=""

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
        br.set_proxies({"http": "http://" + proxy})
        br.open('http://automation.whatismyip.com/n09230945.asp', timeout=10)

        if br.response().read() == ip:
            return False
            print "Not a real proxy"

        return True

    except Exception, e:
        print e
        return False

def mainchecker(proxies, ip, filetosaveto):
    for i in proxies:
        check = checkproxy(i, ip)
        if check:
            open(filetosaveto, 'a').write(i+'\n')
            print "Found {0} working".format(i)
        else:
            print "Proxy {0} is not working".format(i)


def main():
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0')]
    try:
        br.open('http://automation.whatismyip.com/n09230945.asp', timeout=10)
    except:
        exit(0)
    ip = br.response().read()
    proxies = open(raw_input("File with proxies: "), 'r').read().split('\n')
    filetosaveto = raw_input("File to save the working proxies into: ")
    proxies = chunkIt(proxies, 10)
    for a in proxies:
        Thread(target=mainchecker, args=(a, ip, filetosaveto)).start()
    while 1:
        pass

main()
