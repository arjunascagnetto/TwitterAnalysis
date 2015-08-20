#consumer key, consumer secret, access token, access secret.
consumer_key = "qhuyCvdjyOSMoaOqygSuvwxfb"
consumer_secret = "WQ22CUgB2mzruaaq3JzhJUwtnRM9VJKfb3luakxCzoDvClEhou"
access_key = "3360102225-wnRQZynwxFa9SDRkTRkpHH6rGrzD9KKaTvpy8g5"
access_secret = "KTncJcU5UrWbXpHRpX9J7HLmUxqnUcL2gPxGigbIH6Y3Y"

### code to save tweets in json###
import sys
import tweepy
import json

if len(sys.argv) != 3:
	print "usage: tweepy2file 'nomefile' 'query' "
	sys.exit()



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
file = open(sys.argv[1], 'a')

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print status.text

    def on_data(self, data):
#        json_data = json.loads(data)
        file.write(str(data))

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=[sys.argv[2]])
