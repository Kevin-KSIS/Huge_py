import gdata.youtube
import gdata.youtube.service
import random
import urllib
from BeautifulSoup import BeautifulSoup
yt_service = gdata.youtube.service.YouTubeService()
yt_service.developer_key = 'AI39si6VAaDCexeGWcT83JbEVJBiInbk3EZwpEQ6enrk59-UwFcsfc4LPGS5XXI99ieP-2hGrglDB3UrkqWJdLy9Pt6Gm92ZlA'
yt_service.source = 'Testing'
yt_service.client_id = 'my-example-application'


filex = open(raw_input("Enter the name of the file to open:\n")).readlines()
video_id = raw_input("Video ID:\n")
video_entry = yt_service.GetYouTubeVideoEntry(video_id=video_id)

do1 = raw_input("Do you want to comment [y/n] ")
if do1.startswith('y'):
    my_comments = open(raw_input("File with comments:\n")).readlines()

do2 = raw_input("Do you want to subscribe [y/n] ")
if do2.startswith('y'):
    try:
        urlofyoutube = urllib.urlopen('http://www.youtube.com/watch?v=' + video_id).read()
        accountid = BeautifulSoup(urlofyoutube).find('span', 'yt-user-name ').contents[0]
    except:
        print "Could not take the youtube ID!"
        do2 = 'n'

do4 = raw_input("Do you want to favorite [y/n] ")

do3 = raw_input("Do you want to flag [y/n] ")
if do3.startswith('y'):
    complaint_term = raw_input('Reason to flag: ')
    complaint_text = raw_input('Complaint Text:\n')



for a in filex:
    try:
        self.comment = my_comments[random.randint(0,(int(len(my_comments))-1))].rsplit()[0]
    except:
        pass
    try:
        cont = a.rsplit()[0].split(':')
        user = cont[0]
        pwd = cont[1]
        yt_service.email = user
        yt_service.password = pwd
        try:
            yt_service.ProgrammaticLogin()
        except:
            print "Could not login with " + user
            continue
        if do1.startswith('y'):
            try:
                 new_comment = yt_service.AddComment(comment_text=comment, video_entry=video_entry)
                if isinstance(new_comment, gdata.youtube.YouTubeSubscriptionEntry):
                    print 'New comment "' + comment + '" added with ' + user
            except:
                print "Could not comment with the account " + user

        if do2.startswith('y'):
            try:
                new_subscription = yt_service.AddSubscriptionToChannel(
          username_to_subscribe_to=accountid)
                if isinstance(new_subscription, gdata.youtube.YouTubeSubscriptionEntry):
                    print 'New subscription added with ' + user
            except:
                print "Could not susbcribe with the account " + user

        if do3.startswith('y'):
            try:
                 video_entry = yt_service.AddComplaint(self.complaint_text, self.complaint_term, self.video_id)
                 if isinstance(video_entry, gdata.youtube.YouTubeSubscriptionEntry):
                     print 'New flag with ' + user
            except:
                print "Could not flag with the account " + user

        if do4.startswith('y'):
            try:
                response = yt_service.AddVideoEntryToFavorites(video_entry)
                if isinstance(response, gdata.youtube.YouTubeVideoEntry):
                    print 'New favorite with ' + user
            except:
               print "Could not favorite with the account " + user 
            

            
        x+=1
    except:
        cont = a.rsplit()[0].split(':')
        user = cont[0]
        print "Could not do it with the account " + user
        
        
    
