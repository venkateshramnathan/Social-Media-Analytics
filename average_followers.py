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

#path = 'florida/'
path = 'washington/'
complete_json_list = list()
for filename in os.listdir(path):
    # print filename
    with open('{}{}'.format(path, filename), 'r') as json_infile:
        complete_json_list.append(json.load(json_infile))

# print complete_json_list[0]['user']['followers_count']

followers_list = list()
for json_tweet in complete_json_list:
    tb = TextBlob(json_tweet['text'])
    if -1 < tb.sentiment.polarity < -0.5:
        followers_list.append(float(json_tweet['user']['followers_count']))


print 'Average followers:', float(sum(followers_list))/len(followers_list)
