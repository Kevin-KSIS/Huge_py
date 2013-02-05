from mechanize import Browser
import mechanize
import threading
import os , glob, commands, re
import time
import random
#https://api.twitter.com/1/users/profile_image?screen_name=twitterapi&size=bigger

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

#################Begining of class Get get_pics   #####################
class get_pics(threading.Thread):
    def __init__(self, id, userlist,proxy):
        self.id = id
        self.running = False
        threading.Thread.__init__(self)
        self.userlist = userlist
        self.proxy = proxy

    #generate a browser
    def createbrowser(self):
        global proxy_file
        global proxy_index
        br = Browser()
        br.set_handle_gzip(True)
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1 like Mac OS X; en-US) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3')]
        if self.proxy != "":
            br.set_proxies({"http": self.proxy})
        return br

    #get the captcha response
    def saveimage(self,br,user):
        try:
            image = br.response().read()
            writing = open("images/"+user+".gif", 'wb')
            writing.write(image)
            writing.close()
        except:
            pass

    #main run function
    def run(self):
        number = 0
        for user in self.userlist:
            try:
                while user.endswith("\n"):
                    user = user[:-1]
                while user.endswith("\r"):
                    user = user[:-1]
                try:
                    br = self.createbrowser()
                except Exception, e:
                    if self.proxy != "":
                        proxy_file.remove(proxy_file[proxy_index])
                        proxy = proxy_file[proxy_index]
                        number = 0
                    else:
                        pass
                br.open("https://api.twitter.com/1/users/profile_image?screen_name="+user+"&size=bigger")

                self.saveimage(br,user)
            except Exception, e:
                print e
                if self.proxy != "":
                    proxy_file.remove(proxy_file[proxy_index])
                    proxy = proxy_file[proxy_index]
                    number = 0
            if self.proxy != "":
                number+=1
            if number == 140:
                proxy_file.remove(proxy_file[proxy_index])
                proxy = proxy_file[proxy_index]
                number = 0

################# END  of  class  Get  get_pics  #####################

#################Begining of class Get get_status   #####################
class get_status(threading.Thread):
    def __init__(self, id, userlist,proxy):
        self.id = id
        self.running = False
        threading.Thread.__init__(self)
        self.userlist = userlist
        self.proxy = proxy

    #generate a browser
    def createbrowser(self):
        global proxy_file
        global proxy_index
        br = Browser()
        br.set_handle_gzip(True)
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1 like Mac OS X; en-US) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3')]
        if self.proxy != "":
            br.set_proxies({"http": self.proxy})
        return br

    #get the captcha response
    def savestatus(self,br):
        try:
            description = re.findall("description\":\"(.*)\",\"url\"",br.response().read())[0]
            if description not in open("my_status.txt",'r').read():
                open("my_status.txt",'a').write(description+"\n")
        except:
            pass

    #main run function
    def run(self):
        number = 0
        for user in self.userlist:
            try:
                while user.endswith("\n"):
                    user = user[:-1]
                while user.endswith("\r"):
                    user = user[:-1]
                try:
                    br = self.createbrowser()
                except Exception, e:
                    if self.proxy != "":
                        proxy_file.remove(proxy_file[proxy_index])
                        proxy = proxy_file[proxy_index]
                        number = 0
                    else:
                        pass
                br.open("https://api.twitter.com/1/users/show.json?screen_name="+user+"&include_entities=true")
                self.savestatus(br)

            except Exception, e:
                print e
                if self.proxy != "":
                    proxy_file.remove(proxy_file[proxy_index])
                    proxy = proxy_file[proxy_index]
                    number = 0
            if self.proxy != "":
                number+=1
            if number == 140:
                proxy_file.remove(proxy_file[proxy_index])
                proxy = proxy_file[proxy_index]
                number = 0
################# END  of  class  Get  get_status  #####################

#################Begining of class Get get_users   #####################
class get_users(threading.Thread):

    def __init__(self, id, userlist,userlist_tosaveto,proxy):
        self.id = id
        self.running = False
        threading.Thread.__init__(self)
        self.userlist = userlist
        self.userlist_tosaveto = userlist_tosaveto
        self.proxy = proxy

    #generate a browser
    def createbrowser(self):
        global proxy_file
        global proxy_index
        br = Browser()
        br.set_handle_gzip(True)
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1 like Mac OS X; en-US) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3')]
        if self.proxy != "":
            try:
                br.set_proxies({"http": self.proxy})
            except:
                pass
        return br

    #get the captcha response
    def savesusers(self,br):
        try:
            #newusers = re.findall("screen_name\":\"([[0-9]*[a-z]*[-]*[_]*[0-9]*[A-Z]*[0-9]*]*)\",\"profile_background_tile",br.response().read())
            newusers = re.findall("screen_name\":\"([[0-9]*[a-z]*[-]*[_]*[0-9]*[A-Z]*[0-9]*]*)\"",br.response().read())

            print newusers
            for user in newusers:
                if user not in open(self.userlist_tosaveto, 'r').read() and user not in self.userlist:
                    print user
                    open(self.userlist_tosaveto, 'a').write(user+"\n")
        except Exception, e:
            pass


    #main run function
    def run(self):
        number = 0
        for user in self.userlist:
            try:
                while user.endswith("\n"):
                    user = user[:-1]
                while user.endswith("\r"):
                    user = user[:-1]
                try:
                    br = self.createbrowser()
                    br.open("http://api.twitter.com/1/statuses/followers/"+user+".json")
                except Exception, e:
                    if self.proxy != "":
                        proxy_file.remove(proxy_file[proxy_index])
                        proxy = proxy_file[proxy_index]
                        number = 0
                    else:
                        pass
                self.savesusers(br)
            except Exception, e:
                print e
                if self.proxy != "":
                    proxy_file.remove(proxy_file[proxy_index])
                    proxy = proxy_file[proxy_index]
                    number = 0
            if self.proxy != "":
                number+=1
            if number == 140:
                proxy_file.remove(proxy_file[proxy_index])
                proxy = proxy_file[proxy_index]
                number = 0
################# END  of  class  Get  get_users  #####################


#################Begining of class changepic   #####################
class get_status(threading.Thread):
    def __init__(self, id, userlist,proxy):
        self.id = id
        self.running = False
        threading.Thread.__init__(self)
        self.userlist = userlist
        self.proxy = proxy

    #generate a browser
    def createbrowser(self):
        global proxy_file
        global proxy_index
        br = Browser()
        br.set_handle_gzip(True)
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1 like Mac OS X; en-US) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3')]
        if self.proxy != "":
            br.set_proxies({"http": self.proxy})
        return br

    #get the captcha response
    def savestatus(self,br):
        try:
            description = re.findall("description\":\"(.*)\",\"url\"",br.response().read())[0]
            if description not in open("my_status.txt",'r').read():
                open("my_status.txt",'a').write(description+"\n")
        except:
            pass

    #main run function
    def run(self):
        number = 0
        for user in self.userlist:
            https://twitter.com/sessions
            session%5Busername_or_email%5D=venamresm&session%5Bpassword%5D=666123abc
br.select_form(nr=2)

                                        os.chdir(girldirectory)
                            picture = girldirectory + random.choice(glob.glob('*'))
                        br.form.add_file(open(picture), 'text/plain', picture, name='pic')

################# END  of  class  Get  changepic  #####################

proxy_file = ""
proxy_index = 0


def Menu():
    global proxy_file
    global proxy_index
    choice = input("What do you wanna do?\n[1]Get Pictures from a list of users\n[2]Get status from a list of users\n[3]Spider some usernames\n[4]change Pictures and Status of some twitters\n=>  ")
    ##proxy support
    proxysupport = raw_input("Do you want to have proxy support? [y/n]\n=> ")
    if proxysupport =='n':
        proxysupport = False
    else:
        proxysupport = True
        proxy_file = [i.replace('\n', '').replace('\r', '') for i in open(raw_input("Enter the location of the proxy list:\n=> ")).readlines()]
        proxy_index = 0
        proxy = proxy_file[proxy_index]

    ##
    if choice == 1:
        userlist = open(raw_input("Enter the file containing users\n=> ")).readlines()
        nbthread= input("Enter the Number of threads running at the same time:\n=> ")
        z = chunkIt(userlist, nbthread)
        for i, i2 in enumerate(z):
            proxy = ""
            if proxysupport:
                proxy = proxy_file[proxy_index]
            Mythread = get_pics(i,i2,proxy)
            #self.mythreads.append(Mythread)
            Mythread.start()
            if proxysupport:
                proxy_file.remove(proxy_file[proxy_index])
        proxy_index=0

    if choice == 2 :
        userlist = open(raw_input("Enter the file containing users\n=> ")).readlines()
        nbthread= input("Enter the Number of threads running at the same time:\n=> ")
        z = chunkIt(userlist, nbthread)
        for i, i2 in enumerate(z):
            proxy = ""
            if proxysupport:
                proxy = proxy_file[proxy_index]
            Mythread = get_status(i,i2,proxy)
            #self.mythreads.append(Mythread)
            Mythread.start()
            if proxysupport:
                proxy_file.remove(proxy_file[proxy_index])
        proxy_index=0
    if choice == 3 :
        userlist = open(raw_input("Enter the file containing users\n=> ")).readlines()
        userlist_tosaveto = raw_input("Enter the file that will contains new users\n=> ")
        nbthread= input("Enter the Number of threads running at the same time:\n=> ")
        z = chunkIt(userlist, nbthread)
        for i, i2 in enumerate(z):
            proxy = ""
            if proxysupport:
                proxy = proxy_file[proxy_index]
            Mythread = get_users(i,i2,userlist_tosaveto,proxy)
            #self.mythreads.append(Mythread)
            Mythread.start()
            if proxysupport:
                proxy_file.remove(proxy_file[proxy_index])
        proxy_index=0
    if choice ==4:
        print "[*] Not yet included!!"

Menu()
