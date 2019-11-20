import tweepy
import time
import json

def get_credentials():
    t = open("config/credentials.json")
    j = json.loads(t.read())
    t.close()
    return j

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status: tweepy.Status):
        auth = tweepy.OAuthHandler(get_credentials()['consumer_key'], get_credentials()['consumer_secret'])
        auth.set_access_token(get_credentials()['access_token'], get_credentials()['access_token_secret'])
        self.api = tweepy.API(auth)
        if status.user.screen_name == "Fodase_Bot":
            if not status.text.startswith("RT") and not status.text.startswith("@"):
                if status.text.startswith("Foda-se"):
                    ww = status.text.split(" ")[1:]
                    word = ""
                    for w in ww:
                        word += w + " "
                    content = f"*Amamos {word}💜"
                    self.api.update_status(content, status.id, auto_populate_reply_metadata=True)
                    print(f"[**] Novo post: {content}")
        
def create_stream(api: tweepy.API):
    print("[--] Stream iniciado [--]")
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    myStream.filter(follow=["993546816800124928"])
