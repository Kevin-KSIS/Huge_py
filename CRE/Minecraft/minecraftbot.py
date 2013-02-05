import mechanize
import re
import deathbycaptcha

from random import choice
from threading import Thread




class DBC(deathbycaptcha.SocketClient):
    def __init__(self, username, password):
        deathbycaptcha.SocketClient.__init__(self, username, password)

    def getcaptcha(self, captcha):
        self.captcha = self.decode(captcha, 20)
        return self.captcha['text']

    def notsolved(self):
        client.report(self.captcha["captcha"])

        


def genbrowser():
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.addheaders = [('User-agent', 'Mozilla/5.1 (X11; Linux i686; rv:10.0.2) Gecko/20100101 Firefox/10.0.2')]
    return br


def genrandom():
    x = ''
    for i in range(6):
        x+=choice('abcefghiklmnopqrstuvwxzya230')
    return x

class minecraftserver(Thread):
    def __init__(self, page, proxies):
        self.page = page
        self.proxies = proxies
        Thread.__init__(self)

    def run(self):
        for proxy in self.proxies:
            self.br = genbrowser()
            self.br.open('http://www.google.com/recaptcha/api/challenge?k=6Lfa-8QSAAAAANNS4WuTuvYi8Egq573CrG1OBKPV')
            self.captchaid = re.findall("challenge : '(.*)',\n    is_", self.br.response().read())[0]
            print self.captchaid
            self.br.open('http://www.google.com/recaptcha/api/image?c={0}'.format(self.captchaid))
            open('captcha.jpeg', 'wb').write(self.br.response().read())
            reponse = raw_input("Captcha: ")
            self.br = genbrowser()
            print proxy
            self.br.set_proxies({"http": proxy})
            self.br.open(self.page)
            re1 = re.findall('name="(.*-.*)" value="Yes, I wish to vote for this server.', self.br.response().read())[0]
            print re1
            self.br.open(self.page,'recaptcha_challenge_field={0}&recaptcha_response_field={1}&{2}=Yes%2C+I+wish+to+vote+for+this+server.'.format(self.captchaid, reponse, re1), timeout=30)
            open('xd.html', 'w').write(self.br.response().read())
            
            
    
class mcserverstatus(Thread):
    def __init__(self, id, proxies, listofnames):
        self.id = id
        self.proxies = proxies
        self.listofnames = listofnames
        Thread.__init__(self)

    def run(self):
        for proxy in self.proxies:
            try:
                self.br = genbrowser()
                self.br.set_proxies({"http": proxy})
                self.br.open('http://mcserverstatus.com/CaptchaSecurityImages.php')
                open('captcha.jpeg', 'wb').write(self.br.response().read())
                reponse = raw_input("Captcha : ")
                self.br.open('http://mcserverstatus.com/votepost.php?action=postgood&id={0}&userid=0&username=aaaxxa&security_check={1}'.format(self.id, reponse))
                
                
            except Exception, e:
                print e
                

class planetminecraft(Thread):
    def __init__(self, page, proxies, listofnames):
        self.page = page
        self.proxies = proxies
        self.listofnames = listofnames
        Thread.__init__(self)

    def run(self):
        for proxy in self.proxies:
            try:
                self.br = genbrowser()
                self.br.open('http://www.google.com/recaptcha/api/challenge?k=6LcZlM8SAAAAAPP3gQ2b9Zos1Vw7dhb3SA4fL9Ad')
                self.captchaid = re.findall("challenge : '(.*)',\n    is_", self.br.response().read())[0]
                print self.captchaid
                self.br.open('http://www.google.com/recaptcha/api/image?c={0}'.format(self.captchaid))
                open('captcha.jpeg', 'wb').write(self.br.response().read())
                reponse = raw_input("Captcha : ")
                self.br = genbrowser()
                print proxy
                self.br.set_proxies({"http": proxy})
                self.br.open(self.page,'recaptcha_challenge_field={0}&recaptcha_response_field={1}'.format(self.captchaid, reponse), timeout=30)
                open('lol.html', 'w').write(self.br.response().read())
            except Exception, e:
                print e

class minestatus(Thread):
    def __init__(self, page, proxies):
        self.page = page
        self.proxies = proxies
        Thread.__init__(self)

    def run(self):
        for proxy in self.proxies:
            try:
                self.br = genbrowser()
                self.br.open('http://www.google.com/recaptcha/api/challenge?k=6LfcLsoSAAAAAKdvh4z39o1lQ4z2_rYwXuWh2lfb&error=expression')
                self.captchaid = re.findall("challenge : '(.*)',\n    is_", self.br.response().read())[0]
                print self.captchaid
                self.br.open('http://www.google.com/recaptcha/api/image?c={0}'.format(self.captchaid))
                open('captcha.jpeg', 'wb').write(self.br.response().read())
                reponse = raw_input("Captcha : ")
                self.br = genbrowser()
                print proxy
                self.br.set_proxies({"http": proxy})
                self.br.open(self.page,'vote%5Bminecraft_username%5D=trolljunior&recaptcha_challenge_field={0}&recaptcha_response_field={1}'.format(self.captchaid, reponse), timeout=30)
                open('lol.html', 'w').write(self.br.response().read())
            except Exception, e:
                print e

            
def main():
    page = raw_input("Minecraft page: ")
    minestatus(page, open('workingproxies.txt', 'r').read().split('\n')).start()
    
if __name__=='__main__':
    main()


