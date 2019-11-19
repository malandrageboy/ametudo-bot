import tweepy
import json
import time
import random
from stream import create_stream
from datetime import datetime
import pytz
import threading

def get_credentials():
    t = open("config/credentials.json")
    j = json.loads(t.read())
    t.close()
    return j

def get_random_word():
    file = open("config/palavras.txt", encoding="utf-8")
    text = file.read()
    file.close()
    palavras = text.split("\n")
    palavra = random.choice(palavras)
    return palavra

def bot(api: tweepy.API):
    print("[--] Thread iniciado [--]")
    while True:
        now = datetime.now(pytz.timezone("America/Sao_Paulo"))
        if str(now.minute).endswith("30"):
            content = f"Amo {get_random_word()} 💜"
            api.update_status(content)
            print(f"[**] Novo post: {content}")
            time.sleep(60 + 5)

def main():
    # python src/main.py
    auth = tweepy.OAuthHandler(get_credentials()['consumer_key'], get_credentials()['consumer_secret'])
    auth.set_access_token(get_credentials()['access_token'], get_credentials()['access_token_secret'])

    api = tweepy.API(auth)
    th = threading.Thread(target=bot, args=(api,))
    th.start()
    try:
        create_stream(api)
    except:
        print("[!!] ERRO NO STREAM, REINICIANDO...")
        main()

def cu():
    auth = tweepy.OAuthHandler(get_credentials()['consumer_key'], get_credentials()['consumer_secret'])
    auth.set_access_token(get_credentials()['access_token'], get_credentials()['access_token_secret'])

    api = tweepy.API(auth)
    content = "*Amamos liame 💜"
    api.update_status(content, 1196895932190789634, auto_populate_reply_metadata=True)

if __name__ == "__main__":
    # main()
    cu()