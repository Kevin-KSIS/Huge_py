import mechanize
import re

def genbrowser():
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.addheaders = [('User-agent', 'Mozilla/5.1 (X11; Linux i686; rv:10.0.2) Gecko/20100101 Firefox/10.0.2')]
    return br

def main():
    proxies = open(raw_input("File with proxies: ")).read().split('\n')
    for proxy in proxies:
        try:
            br = genbrowser()
            br.set_proxies({"http": proxy})
            br.addheaders = [('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'),
                             ('Cookie' , 'BIGipServerPolopoly_pool=; BIGipServerwww10_pool=')]
            br.open('http://www.nrk.no/nyheter/distrikt/ostafjells/telemark/1.8143661', timeout=30)
            for a in br.addheaders:
                print a
            contentid = re.findall('<input type="hidden" name="contentId" value="(.*)" /', br.response().read())[0].split('"')[0]
            print contentid
            br.open('http://www.nrk.no/contentfile/ajax/returiapoll_post.jsp', 'id=8178&contentId={0}&answer=alt10&vote=Stem'.format(contentid),timeout=30)
            print "Made a new vote"
           
            open('lolx.html', 'w').write(br.response().read())
        except Exception, e:
            print e
            
        
if __name__=='__main__':
    main()
