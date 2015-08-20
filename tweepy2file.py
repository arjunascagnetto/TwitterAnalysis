#consumer key, consumer secret, access token, access secret.
consumer_key = "your"
consumer_secret = "your"
access_key = "your"
access_secret = "your"

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
