"""
    Name: Gaurav Vivek Kolekar
    Mav Id: 1001267145
"""
# importing nltk
import nltk

# importing json
import json

# importing os
import os

# importing matplotlib
import matplotlib.pyplot as plt

# importing wordcloud
from wordcloud import WordCloud

# importing stemmer
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
stopwords = nltk.corpus.stopwords.words('english')

custom_stopwords = [u'trump', u'trump!', u'trump\'', u'"trump \'', u'trumps', u'rt', u'@donaldtrump', u'@realdonaldtrump']
# extending stopword list
stopwords.extend(custom_stopwords)

# stopword removal and stemming
wordcloud_text = ''
# path = 'florida/'
# path = 'washington/'
path = 'all/'
for filename in os.listdir(path):
    # print filename
    with open('{}{}'.format(path, filename), 'r') as json_infile:
        tweet_text = json.load(json_infile)['text']
        # print tweet_text
        for word in tweet_text.split():
            if len(word) == 1 or word.lower() in stopwords or word.startswith('https'):
                continue
            word = ps.stem(word)
            wordcloud_text += ' {}'.format(word.encode('utf-8'))

# print wordcloud_text
wordcloud = WordCloud(max_font_size=40).generate(wordcloud_text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
# plt.savefig('florida_wordcloud.png')
# plt.savefig('washington_wordcloud.png')
plt.savefig('all_wordcloud.png')
plt.show()
