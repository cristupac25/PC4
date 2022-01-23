from modulo import datos
import re
path = './src/re/short_tweets.csv'
analisis_sentimientos = datos.read_pandas(path,780,782)
for tweet in analisis_sentimientos:
    print(tweet)
regex = r'[A,E,I,O,Ua,e,i,o,u.txt]{3,6}'