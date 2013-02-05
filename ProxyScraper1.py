

import urllib, re
import time



##This will hopepully clear the screen

def clearscreen(numlines=100):
 """Clear the console.

 numlines is an optional argument used only as a fall-back.
 """
 import os
 if os.name == "posix":
 # Unix/Linux/MacOS/BSD/etc
 	os.system('clear')
 elif os.name in ("nt", "dos", "ce"):
 # DOS/Windows
 	os.system('CLS')
 else:
 # Fallback for other operating systems.
 	print '\n' * numlines

##end clear screen

clearscreen()

print "Welcome to Proxy Scrape 1.0"

#Choose file to output proxies too

filename = raw_input("Enter Name Of Save File:")

#Open chosen file to write

proxies = open(filename, "w")

print "Scraping Sites this may take a minute"

sites = ['http://elite-proxies.blogspot.com/', 'http://www.proxies.cz.cc/',
        'http://www.proxylists.net/http.txt', 'http://www.proxylists.net/http_highanon.txt',
        'http://multiproxy.org/txt_all/proxy.txt'
        'http://www.digitalcybersoft.com/ProxyList/fresh-proxy-list.shtml',
        'http://tools.rosinstrument.com/proxy/?rule1', 'http://www.scrapeboxproxies.cz.cc/',
        'http://proxylist.j1f.net/', 'http://proxies.my-proxy.com/',
        'http://www.proxy-server.info/proxy-server-list.shtml',
        'http://www.proxyserverprivacy.com/free-proxy-list.shtml']


for site in sites:
    content = urllib.urlopen(site).read()
    e = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+", content)

    for proxy in e:
        proxies.writelines(proxy + '\n')

#Hopefully this will tell me how many proxies i scraped


file = open(filename)

lines = 0
for line in file:
# line is ignored here, but it contains each line of the file,
# including the newline
	lines += 1

print '%r now contains %r Proxies' % (filename, lines)

# end of proxy count 

print "Your proxies are in the install folder under the name", filename

time.sleep(10)
