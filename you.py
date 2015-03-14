import pafy
url = "https://www.youtube.com/watch?v=1ZLFPOynC5s"
video = pafy.new(url)
print "Title= " +video.title
print "Rating= "
print video.rating
print "Author= " +video.author
print "Duration= " +video.duration
print "Likes="
likes = video.likes
print likes
print "Dislikes="
print video.dislikes
print "Views= "
print video.viewcount

