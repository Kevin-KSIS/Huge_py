import gdata.youtube.service
yts = gdata.youtube.service.YouTubeService()
vid = raw_input("Enter the video's ID (Exemple JE5kkyucts8):\n")
urlex = 'http://gdata.youtube.com/feeds/api/videos/' + \
       vid+'/comments?start-index=%d&max-results=25'
index = 1
url = urlex % index
comments = []
while url:
  try:  
      ytfeed = yts.GetYouTubeVideoCommentFeed(uri=url)
      comments.append([ comment.content.text for comment in ytfeed.entry ])
      url = ytfeed.GetNextLink().href
      print url
  except:
      break

filex = raw_input("Enter the file in which you want to save the comments:\n")
for a in comments:
  for x in a:
      fileopen = open(filex, 'a')
      fileopen.write(x+'\n')
      fileopen.close()
      

             
