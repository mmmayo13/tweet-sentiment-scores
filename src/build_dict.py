"""
@filename:          build_dict.py
@author:            Matthew Mayo
@modified:          2014-04-25
@description:       Computes sentiment scores for tweet words *not* appearing
                    in the existing sentiment dictionary file; optional (and
                    recommended) redirector (>) and <newsent_filename> will pipe
                    term sentiment scores into a new sentiment file, useful for
                    later usage
@usage:             python build_dict.py <sentiment_file> <tweet_file> > <newsent_filename>
"""

import sys
import json


"""
Processes tweets looking for existing sent values and unsented words
"""
def proc_tweets(tweet_file, sent_dict):

    unsented_words_dict = {}

    # Process tweets
    for line in tweet_file:
        
        try:
            tweet = json.loads(line)

            try:
                place = tweet["place"]
                lang = tweet["lang"]
                
                # Only consider English tweets from US
                if (place["country_code"] == "US" and lang == "en"):
                    tweet_text = tweet["text"]
                    sent = get_sent(sent_dict, tweet_text)
                    new_tweet_words = get_unsented_words(sent_dict, tweet_text)

                    # Process words in tweet without assigned sentiment value
                    for word in new_tweet_words:
                        try:
                            unsented_words_dict[word].append(sent)
                        except(KeyError):
                            if word != "":
                                unsented_words_dict[word] = []
                                unsented_words_dict[word].append(sent)

            except(KeyError, TypeError):
                pass

        except(KeyError):
            pass

    return unsented_words_dict


"""
Processes the text of a tweet word by word and returns sentiment value
"""
def get_sent(sent_dict, tweet_text):

    tweet_sent = 0

    # Processes tweet word by word
    tweet_words = (tweet_text.replace('\n', ' ').replace('\t', ' ').replace(',', ' ').replace('.', ' ').rsplit(' '))
    for word in tweet_words:
        try:
            tweet_sent = tweet_sent + sent_dict[word]
        except(KeyError):
            pass

    return tweet_sent


"""
Find words not in sentiment dictionary
"""
def get_unsented_words(sent_dict, tweet_text):

    unsented_words = []

    # Processes dictionary identifying words without sentiment value
    words = (tweet_text.replace('\n', '').replace('\t', '').replace(',', '').replace('.', '').rsplit(' '))
    for word in words:
        try:
            sent_dict[word]
        except(KeyError):
            unsented_words.append(word)

    return unsented_words


"""
Parse sentiment file and build a dictionary of word sentiment values
"""
def build_sent_dict(sent_file):

    sent_dict = {}

    # Process sent file line by line
    for line in sent_file:
        sent_item = line.replace('\n', '').rsplit('\t')
        sent_dict[sent_item[0]] = float(sent_item[1])

    return sent_dict


"""
Compute sentiment value for terms in unsented_words_dict
"""
def compute_sent(unsented_words_dict):

    for new_term, tweet_sents in unsented_words_dict.iteritems():
        sent_avg = (float(sum(tweet_sents)) / float(len(tweet_sents)))
        print new_term.encode('utf-8') + "\t" + str(sent_avg)


def main():

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sent_dict = build_sent_dict(sent_file)
    unsented_words_dict = proc_tweets(tweet_file, sent_dict)
    compute_sent(unsented_words_dict)

if __name__ == '__main__':
    main()

