"""
    Name: Gaurav Vivek Kolekar
    Mav Id: 1001267145
"""

# importing library
import tweepy

# importing json
import json

# importing twitter credentials
from twitter_credentials import twitter_credentials as tw_cred


class StreamListener(tweepy.StreamListener):

    def __init__(self):
        super(StreamListener, self).__init__()
        self.number_of_tweets = 10
        self.keyword_search = u'trump'
        # self.keyword_state = 'FLORIDA'
        # self.keyword_state = 'WASHINGTON'
        self.keyword_state = 'ALL'

    def on_status(self, status):
        if status.text.lower().find(self.keyword_search) > -1 and not status.retweeted and status.lang == 'en'\
                and 'RT @' not in status.text and status.in_reply_to_status_id is None:

            json_tweet = json.dumps(status._json, indent=2)
            with open('all/{}_{}.json'.format(self.keyword_state, self.number_of_tweets), 'w') as outfile:
            # with open('washington/{}_{}.json'.format(self.keyword_state, self.number_of_tweets), 'w') as outfile:
            # with open('florida/{}_{}.json'.format(self.keyword_state, self.number_of_tweets), 'w') as outfile:
                outfile.write(json_tweet)
                print self.number_of_tweets
                self.number_of_tweets += 1

        if self.number_of_tweets == 10000:
            return False

    def on_error(self, status_code):
        if status_code == 420:
            return False

if __name__ == '__main__':

    # authentication
    auth = tweepy.OAuthHandler(tw_cred['CONSUMER_KEY'], tw_cred['CONSUMER_SECRET'])
    auth.set_access_token(tw_cred['ACCESS_TOKEN'], tw_cred['ACCESS_TOKEN_SECRET'])

    api = tweepy.API(auth)

    stream_listener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.filter(track=['trump'])
    # stream.filter(locations=[-122.75, 36.8, -121.75, 37.8])
    #stream.filter(locations=[-87.648926, 24.115422, -80.046387, 30.891619])  # florida
    #stream.filter(locations=[-124.644637, 31.980466, -114.822860, 48.944416])  # oregon, washington, california, nevada
    #stream.filter(locations=[-124.715963, 42.026719, -117.027981, 48.967869])  # oregon, washington
    # 439

