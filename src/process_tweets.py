"""
@filename:          process_tweets.py
@author:            Matthew Mayo
@modified:          2014-04-25
@description:       Calculates the sentiment score of tweets stored in
                    <tweet_file> by referencing term-value pairs in the 
                    <sentiment_file>; also calcualtes the length of each tweet;
                    outputs a triple of form [length, sentiment, capture_session]
                    with capture_session based on <tweet_file> name 
@usage:             python process_tweets.py <sentiment_file> <tweet_file>
"""

import sys
import json


"""
Processe the text of a tweet word by word, return sentiment value
"""
def get_sent(sent_dict, tweet_text):

    tweet_sent = 0
    tweet_words = (tweet_text.replace('\n', '').replace('\t', '').replace(',', '').replace('.', '').rsplit(' '))

    # Process tweet
    for word in tweet_words:
        try:
            tweet_sent = tweet_sent + sent_dict[word]
        except(KeyError):
            pass

    return tweet_sent


"""
Parse sentiment file, build a dictionary of word sentiment values
"""
def build_sent_dict(sent_file):

    sent_dict = {}

    # Process sent file line by line
    for line in sent_file:
        sent_item = line.replace('\n', '').rsplit('\t')
        sent_dict[sent_item[0]] = float(sent_item[1])

    return sent_dict


"""
Process tweets, find their sentiment values and lengths
"""
def proc_tweets(sent_dict, tweet_file):

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
                    length = len(tweet_text)
                    # Below partially commented to supress printing of actual tweets
                    print str(length) + "\t" + str(sent) + "\t" + sys.argv[2] # + "\t" + tweet_text.encode('utf-8')
             
            except(KeyError, TypeError):
                pass

        except(KeyError):
            pass


def main():

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sent_dict = build_sent_dict(sent_file)
    proc_tweets(sent_dict, tweet_file)

if __name__ == '__main__':
    main()

