import random
import tweepy
import yaml
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
        
    with urllib.request.urlopen(conf["TWEETS_YAML_URL"]) as tweets_file:
        tweets = yaml.load(tweets_file, Loader=yaml.FullLoader)
        random.seed()
        t = random.choice(tweets)
        print("Publicant:")
        print(t)
        tweet(conf, t)
