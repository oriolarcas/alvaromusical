import random
import time
import tweepy
import yaml
import requests
import urllib

def tweet(conf, text):
    auth = tweepy.OAuthHandler(conf["CONSUMER_KEY"], conf["CONSUMER_SECRET"])
    auth.set_access_token(conf["ACCESS_KEY"], conf["ACCESS_SECRET"])
    api = tweepy.API(auth)

    if len(text) <= 280:
        api.update_status(status=text)

if __name__ == '__main__':
    with open('conf.yaml') as conf_file:
        conf = yaml.load(conf_file, Loader=yaml.FullLoader)

    with response.readlines(urllib.urlopen('https://raw.githubusercontent.com/oriolarcas/alvaromusical/main/musica.yaml')) as tweets_file:
        tweets = yaml.load(tweets_file, Loader=yaml.FullLoader)
        random.seed()
        t = random.choice(tweets)
        print("Publicant:")
        print(t)
        tweet(conf, t)
