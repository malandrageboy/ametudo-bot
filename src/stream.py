import tweepy

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status: tweepy.Status):
        if status.user.screen_name == "Fodase_Bot":
            if not status.text.startswith("RT") and not status.text.startswith("@"):
                print("[**] Novo post: " + status.text)

def create_stream(api: tweepy.API):
    print("[--] Stream iniciado [--]")
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    myStream.filter(follow=["993546816800124928"])
