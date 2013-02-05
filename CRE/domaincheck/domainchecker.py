##Made By venam (aka raptor, aka resm)##
##feel free to modify and use this code as you wish##

###browser##
import mechanize
##threads##
from threading import Thread


############generate a browser########################
def createbrowser():
    br = mechanize.Browser()
    br.set_handle_gzip(True)
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel MacOS X; rv:14.0) Gecko/20100101 Firefox/14.0.1')]
    return br
###################################################


############FUNCTION THAT CUT A FILES IN MANY PARTS######################
def chunkIt(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0
  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg
  return out
###########END OF FUNCTION THAT CUT A FILE IN MANY PARTS##################


###########A List of Domains extensions###############
domainextension = [
".com",
".co",
".info",
".net",
".org",
".me",
".mobi",
".us",
".biz",
".xxx",
".ca",
".mx",
".tv",
".ws",
".ag",
".com.ag",
".net.ag",
".org.ag",
".am",
".asia",
".at",
".be",
".com.br",
".net.br",
".bz",
".com.bz",
".net.bz",
".cc",
".com.co",
".net.co",
".nom.co",
".de",
".es",
".com.es",
".nom.es",
".org.es",
".eu",
".fm",
".fr",
".gs",
".in",
".co.in",
".firm.in",
".gen.in",
".ind.in",
".net.in",
".org.in",
".it",
".jobs",
".jp",
".ms",
".com.mx",
".nl",
".nu",
".co.nz",
".net.nz",
".org.nz",
".se",
".tk",
".tw",
".com.tw",
".idv.tw",
".org.tw",
".co.uk",
".me.uk",
".org.uk"]
######################################################


###functions that takes a list of words [domains] and for each word check the availability of each extension the save it to the second argument [filex]###
def domaincheck(domains,filex):
    for domain in domains:
        br = createbrowser()
        for b in domainextension:
            while domain.endswith("\n") or domain.endswith("\r"):
                domain = domain[:-1]
            br.open("http://www.godaddy.com/domains/search.aspx?ci=54814&isc=cjcmsc001t&domainToCheck="+domain+"&tld="+b+"&checkAvail=1")
            if '<span class="red t18">is already taken' not in br.response().read():
                open(filex,'a').write(domain+b+"\n")
                print "\n["+ bcolors.OKGREEN +"+"+ bcolors.ENDC +"] "+ bcolors.backgreen +domain+b+ bcolors.ENDC +" IS AVAILABLE"
################################


######Colors for terminal#########
class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[1;32m'
        WARNING = '\033[93m'
        FAIL = '\033[0;31m'
        ENDC = '\033[0m'
        CYAN = '\033[1;36m'
        COOL = '\033[0;45m'
        COOL1 = '\033[1;45m'
        backgreen ='\033[1;44m'
##################################


###takes the domain list from the user###
domains = open(raw_input("\n"+ bcolors.COOL +"|---"+ bcolors.COOL1 +" Domain Availability Checker By VENAMTEAM"+ bcolors.COOL +" ---|"+ bcolors.ENDC +"\n\n["+ bcolors.CYAN +"*"+ bcolors.ENDC +"] Enter a list domain to check availablility :\n"+bcolors.OKGREEN +"=>"+bcolors.ENDC +" ")).readlines()
#########################################

##takes the name of the file to save to from the user##
filex = raw_input("\n["+ bcolors.CYAN +"*"+ bcolors.ENDC +"]Location of the File you want to save to :\n"+bcolors.OKGREEN +"=>"+bcolors.ENDC +" ")
#######################################################

##take the number of threads that will run at the same time from the user##
nbthread = input("\n["+ bcolors.CYAN +"*"+ bcolors.ENDC +"]Number of thread running at the same time :\n"+bcolors.OKGREEN +"=>"+bcolors.ENDC +" ")
###########################################################################

##less domains then threads; then threads=number of domains##
if len(domains)<nbthread:
    nbthread=len(domains)
############################################################

##divide the words in the files by the number of threads and starts them###
z = chunkIt(domains,nbthread)
for chinese in z:
    Thread(target=domaincheck, args=(chinese,filex)).start()
###########################################################################
