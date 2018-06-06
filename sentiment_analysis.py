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
#path = 'washington/'
path = 'all/'
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
# print sub_scores
# print polarity_scores

# plotting subjectivity scores
plt.hist(sub_scores)
plt.axvline(float(sum(sub_scores))/len(sub_scores), color='r', linestyle='dashed', linewidth=1)
# plt.title('Subjectivity scores for the state of Florida')
#plt.title('Subjectivity scores for Region 2 (California, Oregon, Washington, and Nevada)')
plt.title('Subjectivity scores 10K tweets')
plt.xlabel('Subjectivity Scores')
plt.ylabel('Sentences')
plt.grid(True)
# plt.savefig('subjectivity_florida.png')
# plt.savefig('subjectivity_washington.png')
plt.savefig('subjectivity_all.png')
plt.show()

# plotting polarity scores
plt.hist(polarity_scores)
plt.axvline(float(sum(polarity_scores))/len(polarity_scores), color='r', linestyle='dashed', linewidth=1)
# plt.title('Polarity scores for the state of Florida')
# plt.title('Polarity scores for Region 2 (California, Oregon, Washington, and Nevada)')
plt.title('Polarity scores for 10K tweets')
plt.xlabel('Polarity Scores ')
plt.ylabel('Sentences')
plt.grid(True)
# plt.savefig('polarity_florida.png')
#plt.savefig('polarity_washington.png')
plt.savefig('polarity_all.png')
plt.show()

print 'subjectivity', float(sum(sub_scores))/len(sub_scores)
print 'polarity', float(sum(polarity_scores))/len(polarity_scores)
