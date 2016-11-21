import json
import pandas as pd
import re
import numpy as np


def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


tweets_data_path = 'data.json'


tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
        
#print (len(tweets_data))

tweets = pd.DataFrame.from_dict(tweets_data)

#print(tweets['lang'].value_counts())

tweets['python'] = tweets['text'].apply(lambda tweet: word_in_text('python', tweet))

print(tweets['python'].value_counts()[True])


