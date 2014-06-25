"""
@filename:          extract_tweets.py
@author:            Matthew Mayo
@modified:          2014-04-25
@description:       Extracts tweet text from <tweet_file> and print out
                    to console; can be redirected to optional <output_file>
@usage:             python extract_tweets.py <tweet_file> > <output_file>
"""

import sys
import json



"""
Process tweets, find their sentiment values and lengths
"""
def proc_tweets(tweet_file):

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
                    print tweet_text.encode('utf-8')
             
            except(KeyError, TypeError):
                pass

        except(KeyError):
            pass


def main():

    tweet_file = open(sys.argv[1])
    proc_tweets(tweet_file)


if __name__ == '__main__':
    main()

