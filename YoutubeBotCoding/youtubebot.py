import gdata.youtube
import gdata.youtube.service
yt_service = gdata.youtube.service.YouTubeService()
yt_service.developer_key = 'AI39si6VAaDCexeGWcT83JbEVJBiInbk3EZwpEQ6enrk59-UwFcsfc4LPGS5XXI99ieP-2hGrglDB3UrkqWJdLy9Pt6Gm92ZlA'
yt_service.source = 'Testing'
yt_service.client_id = 'my-example-application'


filex = open(raw_input("Enter the name of the file to open:\n")).readlines()
video_id = raw_input("Video ID:\n")
video_entry = yt_service.GetYouTubeVideoEntry(video_id=video_id)
my_comment = raw_input("What to comment:\n")
x = 0

for a in filex:
    try:
        cont = a.rsplit()[0].split(':')
        user = cont[0]
        pwd = cont[1]
        yt_service.email = user
        yt_service.password = pwd
        yt_service.ProgrammaticLogin()
        yt_service.AddComment(comment_text=my_comment, video_entry=video_entry)
        x+=1
    except:
        cont = a.rsplit()[0].split(':')
        user = cont[0]
        print "Could not comment with account number " + user
        
        
    
