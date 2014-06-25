## Tweet Sentiment Analysis

### Introduction

Scripts for capturing tweets, creating sentiment dictionary, processing & scoring tweet sentiments, written in Python. These scripts were written to facilitate the clustering of tweet length & sentiment scores in [this research paper](http://arxiv.org/pdf/1406.3287v1.pdf).

Twitter app authentication credentials are required for use of get_tweets.py. Acquire these [here](https://dev.twitter.com/).

Inspiration for some of this material comes from [Bill Howe](http://homes.cs.washington.edu/~billhowe/) and his Coursera course, [Introduction to Data Science](https://www.coursera.org/course/datasci).

### Description

*get_tweets.py*

- Captures tweets from Twitter stream
- Requires keys and secrets in order to successfully run

*build_dict.py*

- Takes existing sentiment dictionary as list of seed words
- Builds new dictionary of unscored tweet words based on tweet mean score of scored existing words

*process_tweets.py*

- Scores the tweets word-by-word based on crafted sentiment dictionary created with build_dict.py

*extract_text.py*

- Extracts the tweet text from the tweet JSON document, optionally saves to file
 
### Usage

The research paper cited above provides detailed explanation and use case examples for utilizing these scripts.

### Requirements

Python (tested with 2.7.7)

### Installation

- No installation; just download and run scripts

```python
# get_tweets.py
python get_tweets.py > <capture_filename>

# build_dict.py
python build_dict.py <sentiment_file> <tweet_file> > <newsent_filename>

# process_tweets.py
python process_tweets.py <sentiment_file> <tweet_file>

# extract_text.py
python extract_tweets.py <tweet_file> > <output_file>
```

### Getting Help

The code is fairly simple and should be easy to follow.

If you require an introduction to sentiment analysis, [check here](http://en.wikipedia.org/wiki/Sentiment_analysis).

### Author

[Matt Mayo](http://about.me/mattmayo)

### License

This software is made available under the [MIT License](http://choosealicense.com/licenses/mit/)
