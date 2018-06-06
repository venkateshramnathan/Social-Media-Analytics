"""
    Name: Gaurav Vivek Kolekar
    Mav Id: 1001267145
"""
#importing json
import json

# importing os
import os

# importing textblob
from textblob import TextBlob

# importing matplotlib
import matplotlib.pyplot as plt

# path = 'florida/'
path = 'washington/'
tweet_text_list = list()
for filename in os.listdir(path):
    # print filename
    with open('{}{}'.format(path, filename), 'r') as json_infile:
        tweet_text_list.append(json.load(json_infile)['text'])

# subjectivity and polarity scores
sub_scores = list()
polarity_scores = list()
for tweet_text in tweet_text_list:
    tb = TextBlob(tweet_text)
    sub_scores += [tb.sentiment.subjectivity]
    polarity_scores += [tb.sentiment.polarity]

#print polarity_scores

pos_counter = 0
neg_counter = 0
for tweet_sentiment in polarity_scores:
    if tweet_sentiment > 0:
        pos_counter += 1
    elif tweet_sentiment < 0:
        neg_counter += 1

print 'pos counter', pos_counter
print 'neg counter', neg_counter
