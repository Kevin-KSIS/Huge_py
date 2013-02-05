import socket
socket.setdefaulttimeout(30)
import mechanize
from threading import Thread
from re import findall

class Run(Thread):

    def __init__(self, proxy_list, link):
        self.proxy_list = proxy_list
        self.link = link
        self.isrunning = False
        Thread.__init__(self)

    def run(self):
        self.isrunning  = True
        for proxy in self.proxy_list:
                if self.isrunning:
                        try:
                                br = mechanize.Browser()
                                br.set_handle_robots(False)
                                br.set_proxies({"http": "http://" + proxy})
                                br.open(self.link, timeout=30)
                                key = findall('''name='key' value='(.*)'/>''', br.response().read())
                                if len(key) == 0:
                                    print "Already voted with {0}".format(proxy)
                                else:
                                    key = key[0]
                                    br.open(self.link, 'key={0}'.format(key), timeout=30)
                                    print "New internet given"
                        except Exception, e:
                            print e
                            print "Error with {0}".format(proxy)
                else:
                        break

    def stop(self):
            self.isrunning = False

Run()
