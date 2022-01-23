from modulo import datos
import re
path = './src/re/short_tweets.csv'
re.findall(r"@\w+\W*\w+", path)
re.search("likes", path)
re.search("retweets", path)