"""
    Name: Gaurav Vivek Kolekar
    Mav Id: 1001267145
"""
# importing os
import os

# importing json
import json

# importing numpy
import numpy as np

# importing nltk
import nltk

# importing count vectorizer and tfidfvectorizer from scikit learn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# importing decomposition from sklearn
from sklearn import decomposition

# importing gensim corpora
from gensim import corpora

# importing models from gensim
from gensim import models

stopwords = nltk.corpus.stopwords.words('english')
custom_stopwords = [u'trump', u'trump!', u'trump\'', u'"trump \'', u'trumps', u'rt', u'@donaldtrump',
                    u'@realdonaldtrump', u'amp']

# extending stopword list
stopwords.extend(custom_stopwords)

tweet_text_corpus = list()
docs = list()
#path = 'florida/'
#path = 'washington/'
path = 'all/'
for filename in os.listdir(path):
    # print filename
    clean_tweet_text = ''
    with open('{}{}'.format(path, filename), 'r') as json_infile:
        tweet_text = json.load(json_infile)['text']
        # print tweet_text
        inner_doc_list = list()
        for word in tweet_text.split():
            # print type(word)
            if len(word) == 1 or word.lower() in stopwords or word.startswith('https'):
                continue
            inner_doc_list.append(word)
            clean_tweet_text += ' {}'.format(word.encode('utf-8'))
    docs.append(inner_doc_list)
    tweet_text_corpus.append(clean_tweet_text)

# print tweet_text_corpus
# print len(tweet_text_corpus)

vectorizer = TfidfVectorizer(stop_words='english', min_df=2)
dtm = vectorizer.fit_transform(tweet_text_corpus)

vocab = vectorizer.get_feature_names()

num_topics = 7
clf = decomposition.NMF(n_components=num_topics, random_state=1)

doctopic = clf.fit_transform(dtm)


topic_words = list()
number_of_topic_words = 5

topic_words = []
num_top_words = 5
for topic in clf.components_:
    # print topic.shape, topic[:5]
    word_idx = np.argsort(topic)[::-1][0:num_top_words]  # get indexes with highest weights
    # print 'top indexes', word_idx
    topic_words.append([vocab[i] for i in word_idx])
    # print topic_words[-1]
    # print

# print '__lol__' * 10


for t in range(len(topic_words)):
    print "Topic {}: {}".format(t, ' '.join(topic_words[t][:15]))

dic = corpora.Dictionary(docs)

corpus = [dic.doc2bow(text) for text in docs]
# print(type(corpus), len(corpus))

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

NUM_TOPICS = 7
model = models.ldamodel.LdaModel(corpus_tfidf,
                                 num_topics=NUM_TOPICS,
                                 id2word=dic,
                                 update_every=1,
                                 passes=100)

print("LDA model")
topics_found = model.print_topics(20)
counter = 1
for t in topics_found:
    print("Topic #{} {}".format(counter, t))
    counter += 1
