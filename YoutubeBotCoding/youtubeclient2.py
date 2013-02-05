from youtube_client import YoutubeClient

client = YoutubeClient()
url = 'http://gdata.youtube.com/feeds/api/users/pr3dat0r002/uploads'
client.get_items(client.yt_service.GetYouTubeVideoFeed(url))

