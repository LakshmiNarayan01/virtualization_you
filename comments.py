import gdata.youtube
import gdata.youtube.service

f = open('comments.txt','w')

youtube_service = gdata.youtube.service.YouTubeService()

# randomly selected, mostly funny, some just stupid and lame
video_ids = ["1ZLFPOynC5s"]

for id in video_ids:
  for comment in youtube_service.GetYouTubeVideoCommentFeed(video_id = id).entry:
    print "..."
    ara = comment.content.text
    print ara
    f.write(ara)

f.close()





