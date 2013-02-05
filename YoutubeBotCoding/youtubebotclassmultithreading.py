import gdata.youtube
import gdata.youtube.service
import random
import urllib
from BeautifulSoup import BeautifulSoup
import thread, threading
import time

class YoutubeBot:
    def __init__(self):
        self.yt_service = gdata.youtube.service.YouTubeService()
        self.yt_service.developer_key = 'AI39si6VAaDCexeGWcT83JbEVJBiInbk3EZwpEQ6enrk59-UwFcsfc4LPGS5XXI99ieP-2hGrglDB3UrkqWJdLy9Pt6Gm92ZlA'
        self.yt_service.source = 'Testing'
        self.yt_service.client_id = 'my-example-application'

    def info(self):
        self.filex = open(raw_input("Enter the name of the file to open:\n")).readlines()
        self.video_id = raw_input("Video ID:\n")
        self.video_entry = self.yt_service.GetYouTubeVideoEntry(video_id=self.video_id)

        self.do1 = raw_input("Do you want to comment [y/n] ")
        if self.do1.startswith('y'):
            self.my_comments = open(raw_input("File with comments:\n")).readlines()

        self.do2 = raw_input("Do you want to subscribe [y/n] ")
        if self.do2.startswith('y'):
            try:
                self.urlofyoutube = urllib.urlopen('http://www.youtube.com/watch?v=' + self.video_id).read()
                self.accountid = BeautifulSoup(self.urlofyoutube).find('span', 'yt-user-name ').contents[0]
                print "Account ID: " + self.accountid
            except:
                print "Could not take the youtube ID!"
                self.do2 = 'n'

        self.do4 = raw_input("Do you want to favorite [y/n] ")

        self.do3 = raw_input("Do you want to flag [y/n] ")
        if self.do3.startswith('y'):
            self.complaint_term = raw_input('Reason to flag: ')
            self.complaint_text = raw_input('Complaint Text:\n')

    def start(self):
        self.x=0
        thread1 = threading.Thread(self.run)
        thread2 = threading.Thread(self.run)
        thread1.start()
        thread2.start()

                



    def run(self):
        while self.x<len(self.filex):
            try:
                self.comment = self.my_comments[random.randint(0,(int(len(self.my_comments))-1))].rsplit()[0]
            except:
                pass
            try:
                cont = self.filex[x].rsplit()[0].split(':')
                user = cont[0]
                pwd = cont[1]
                self.yt_service.email = user
                self.yt_service.password = pwd
                try:
                    self.yt_service.ProgrammaticLogin()
                except:
                    print "Could not login with " + user
                if self.do1.startswith('y'):
                    try:
                       self.yt_service.AddComment(comment_text=self.comment, video_entry=self.video_entry)
                       print 'New comment "' + self.comment + '" added with ' + user
                    except:
                        print "Could not comment with the account " + user

                if self.do2.startswith('y'):
                    try:
                        new_subscription = self.yt_service.AddSubscriptionToChannel(
                  username_to_subscribe_to=self.accountid)
                        if isinstance(new_subscription, gdata.youtube.YouTubeSubscriptionEntry):
                            print 'New subscription added with ' + user
                    except:
                        print "Could not susbcribe with the account " + user

                if self.do3.startswith('y'):
                    try:
                        videoflag = self.yt_service.AddComplaint(self.complaint_text, self.complaint_term, self.video_id)

                        if isinstance(videoflag, gdata.youtube.YouTubeSubscriptionEntry):
                            print 'New flag with ' + user
                    except:
                        print "Could not flag with the account " + user

                if self.do4.startswith('y'):
                    try:
                        self.yt_service.AddVideoEntryToFavorites(self.video_entry)
                        print 'New favorite with ' + user
                    except:
                       print "Could not favorite with the account " + user 
                self.x+=1    

            except:
                cont = a.rsplit()[0].split(':')
                user = cont[0]
                print "Could not do it with the account " + user
                self.x+=1

    def commentgraber(self):
        vid = raw_input("Enter the video's ID (Exemple JE5kkyucts8):\n")
        urlex = 'http://gdata.youtube.com/feeds/api/videos/' + \
                vid+'/comments?start-index=%d&max-results=25'
        index = 1
        url = urlex % index
        comments = []
        while url:
            try:
                ytfeed = self.yt_service.GetYouTubeVideoCommentFeed(uri=url)
                comments.append([comment.content.text for comment in ytfeed.entry ])
                url = self.yt_service.GetNextLink().href
                print url
            except:
                break
        filex = raw_input("Enter the file in which you want to save the comments:\n")
        for a in comments:
            for x in a:
                fileopen = open(filex, 'a')
                fileopen.write(x+'\n')
                fileopen.close()


Mybot = YoutubeBot()
print "1.Bot (Comment/Favorite/Subscriber/Flag)"
print "2.Comment Graber"
print;print;
x = input("What do you want to do? ")
if x == 1:
    Mybot.info()
    Mybot.start()
elif x == 2:
    Mybot.commentgraber()
    


        
