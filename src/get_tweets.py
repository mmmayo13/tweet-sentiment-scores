"""
@filename:          get_tweets.py
@author:            Matthew Mayo
@modified:          2014-04-25
@description:       Authentiates to Twitter, reads tweet data from stream,
                    outputs tweets in JSON format; optional (and recommended)
                    redirector (>) and <capture_filename> will pipe tweets
                    to specified filename, useful for later processing
@usage:             python get_tweets.py > <capture_filename>
"""

import oauth2 as oauth
import urllib2 as urllib

# get your own!
TOKEN_KEY = ""
TOKEN_SECRET = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""

oauth_token = oauth.Token(key = TOKEN_KEY, secret = TOKEN_SECRET)
oauth_consumer = oauth.Consumer(key = CONSUMER_KEY, secret = CONSUMER_SECRET)
signature_method = oauth.SignatureMethod_HMAC_SHA1()

debug_level = 0
http_method = "GET"

http_handler  = urllib.HTTPHandler(debuglevel = debug_level)
https_handler = urllib.HTTPSHandler(debuglevel = debug_level)


"""
Authenticate to Twitter, access the tweet stream
"""
def read_stream(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer, token = oauth_token,
      http_method = http_method, http_url = url, parameters = parameters)
    req.sign_request(signature_method, oauth_consumer, oauth_token)
    encoded_post_data = None
    url = req.to_url()
    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)
    response = opener.open(url, encoded_post_data)
    return response


"""
Output tweet data in json format
"""
def get_tweets():
    url = "https://stream.twitter.com/1/statuses/sample.json"
    parameters = []
    response = read_stream(url, "GET", parameters)
    for line in response:
        print line.strip()


def main():
    get_tweets()

if __name__ == '__main__':
    main()

