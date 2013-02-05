import mechanize, BeautifulSoup, random, time, os , glob, threading, commands, re

girlnames = open('first name girl').readlines()
boynames = open('first name man').readlines()
lastnames = open('last name').readlines()
girldirectory = os.getcwd()+ '/facebook profilepics girl/'
boydirectory = os.getcwd()+'/facebook profilepics man/'
useragents=[]
for passing in open('user-agents').readlines():
    passing = passing[:-1]
    useragents.append(passing)

capuser = 'popopopo'
cappwd = 'popopopo'
capapi= '689a8ba9bc82635447955348dbc20b25'


def genrandom():
    x = random.randint(6,8)
    pw = ''
    for a in xrange(x):
        pw+=random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return pw


def createaccount(filex, trader):
    while 1:
        try:
            br = mechanize.Browser()
            br.set_handle_gzip(True)
            br.addheaders = [('User-agent', random.choice(useragents))]
            br.set_handle_robots(False)
            br.set_handle_redirect(True)
            br2 = mechanize.Browser()
            br2.set_handle_gzip(True)
            br2.addheaders = [('User-agent', random.choice(useragents))]
            br2.set_handle_robots(False)
            br2.open('http://www.inbox.jbi.in')
            br2.select_form(nr=1)
            br2.submit()
            soup = BeautifulSoup.BeautifulSoup(br2.response().read())
            for a in soup.findAll('input'):
                if a.get('name') == 'mail':
                        email =  a.get('value')
                        break
            br.open('http://m.facebook.com/r.php?_rdr')
            br.select_form(nr=0)
            if random.randint(0,1) == 0:
                genre = 'm'
            else:
                genre = 'f'
            if genre == 'm':
                br.form['firstname'] = random.choice(boynames)
            else:
                br.form['firstname'] = random.choice(girlnames)
            br.form['lastname'] = random.choice(lastnames)
            br.form['email'] = email
            if genre=='m':
                br.form['gender'] = ['2']
            else:
                br.form['gender'] = ['1']
            br.form['month'] = [str(random.randint(1,12))]
            br.form['day'] = [str(random.randint(1,28))]
            br.form['year'] = [str(random.randint(1970,1995))]
            password = genrandom()
            br.form['pass'] = password
            br.submit()
            while br.geturl() == 'http://m.facebook.com/r.php?refid=0':
                print "Facebook Likes Captchas!"
                soup = BeautifulSoup.BeautifulSoup(br.response().read())
                for img in soup.findAll('img'):
                    if img.get('src').startswith('/captcha'):
                        image_response = br.open_novisit(img['src'])
                        image = image_response.read()
                        writing = open('captcha.jpeg', 'wb')
                        writing.write(image)
                        writing.close()
                        br.select_form(nr=0)
                        if not trader:
                            threading.Thread(target=commands.getoutput, args=('eog "' + os.getcwd() + '"' + '/captcha.jpeg',)).start()
                            captcha = raw_input("Please enter the captcha: ")
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




                        br.form['captcha_response'] = captcha
                        br.submit(name='captcha_submit_text', label='Submit')
                        break




            print "Waiting for confirmation with " + email
            print br.geturl()
            cond = False
            cond2 = 0
            while cond == False:
                if cond2< 4:
                    time.sleep(5)
                    br2.reload()
                    for a in br2.links(url_regex='facebook'):
                        br.follow_link(a)
                        cond = True
                        break
                    cond2+=1
                else:
                    break
            if cond == True:
                for a in br.links(url_regex='nav.php'):
                    br.follow_link(a)
                    break
                if not 'checkpoint' in br.geturl():
                    opn = open(filex, 'a')
                    opn.write(email+':'+password+'\n')
                    opn.close()
                    print "Created account " + email + " with password " + password
                else:
                    print "Locked"

                try:
                    if not 'checkpoint' in br.geturl():
                        br.select_form(nr=0)
                        if genre == 'm':
                            os.chdir(boydirectory)
                            picture = boydirectory + random.choice(glob.glob('*'))
                        else:
                            os.chdir(girldirectory)
                            picture = girldirectory + random.choice(glob.glob('*'))
                        br.form.add_file(open(picture), 'text/plain', picture, name='pic')
                        br.submit()
                        print "Uploaded avatar with " + email
                except:
                    print "Could not upload a picture with " + email
        except KeyboardInterrupt:
            break
        except:
            print "Error"

        br.close()
        br2.close()

filewriting = raw_input("Where do you want to save the accounts: ")
captchatrader = raw_input("Do you want to use captcha trader? [y/n] ")[0]
if captchatrader == 'y':
    trader=True
else:
    trader=False
createaccount(filewriting, trader)






