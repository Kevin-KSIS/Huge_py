from mechanize import Browser
import threading

def chunkIt(seq, num):
	avg = len(seq) / float(num)
	out = []
	last = 0.0
	while last < len(seq):
		out.append(seq[int(last):int(last + avg)])
		last += avg
	return out

def ask(listz):
    listx = []
    for passx in listz:
        x = raw_input(passx)
        if x.startswith('y'):
            listx.append(True)
        else:
            listx.append(False)
    return listx
    
class normalbot:

    def __init__(self, video, like, dislike,favorite, flag, subscribe, user):
        self.video = video
        self.like = like
        self.dislike = dislike
        self.favorite = favorite
        self.flag = flag
        self.subscribe = subscribe
        self.user = user



    def flag(self, video):
        br.open('http://m.youtube.com/flag?gl=US&hl=en&client=mv-google&v=' + video)
        br.select_form(nr=0)
        br.submit()


    def susbcribe(self, user, br):
        br.open('http://m.youtube.com/profile?gl=US&hl=en&client=mv-google&user=' + user)
        br.select_form(nr=1)
        br.submit()

    def like(self,video, br):
        br.open('http://m.youtube.com/rating?gl=US&hl=en&client=mv-google&action_like=1&v' + video)
        br.select_form(nr=0)
        br.submit()
        
    def dislike(self,video, br):
        br.open('http://m.youtube.com/rating?gl=US&hl=en&client=mv-google&action_dislike=1&v=' + video)
        br.select_form(nr=0)
        br.submit()
        
    def comment(self,video, br, comment):
        br.open('http://m.youtube.com/post_comment?gl=US&hl=en&client=mv-google&v=' + video)
        br.select_form(nr=0)
        br.form['comment'] = comment
        br.submit()

    def favorite(self,video, br):
        br.open('http://m.youtube.com/add_favorite?gl=US&hl=en&client=mv-google&v=' + video)
        br.select_form(nr=0)
        br.submit()

    def do(self, usrl):
        for a in usrl:
            user, passw = a.split(':')
            br = Browser()
            br.set_handle_robots(False)
            br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
            br.open('https://accounts.google.com/ServiceLogin?uilel=3&service=youtube&passive=true&continue=http%3A%2F%2Fm.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26nomobiletemp%3D1%26warned%3D1%26feature%3Dmobile%26next%3D%252Fmy_account%253Fgl%253DUS%2526hl%253Den%2526client%253Dmv-google%26hl%3Den_US&hl=en_US&ltmpl=mobile')
            br.select_form(nr=0)
            br.form['Email'] = user
            br.form['Passwd'] = passw
            br.submit()
            if self.like:
                like(self.video, br)
            if self.dislike:
                try:
                    dislike(self.video, br)
                except:
                    print "Could not dislike with " + user
            if self.comment:
                try:
                    comment(self.video,br,comment)
                except:
                    print "Could not comment with " + user
            if self.favorite:
                try:
                    favorite(self.video, br)
                except:
                    print "Could not favorite with " + user
            if self.flag:
                try:
                    flag(self.video, br)
                except:
                    print "Could not flag with " + user

            if self.subscribe:
                try:
                    subscribe(self.user, br)
                except:
                    print "Could not subscribe with " + user
                 




while 1:
    like = False
    dislike = False
    favorite = False
    flag = False
    subscribe = False
    user = False
    acs = open(raw_input("File with accounts: ")).readlines()
    video = raw_input("Video ID: ")
    listtoask = ['Do you want to like [y/n] ', 'Do you want to dislike [y/n] ', \
                 'Do you want to favorite [y/n] ', 'Do you want to flag [y/n] ', \
                 'Do you want to subscribe [y/n] ']
    like, dislike, favorite, flag, subcribe = ask(listtoask)
    if subscribe:
        user = raw_input("User to subscribe: ")
    Mybot = normalbot(video, like, dislike,favorite, flag, subscribe, user)
    Mybot.do(acs)



    
