import json
import pandas as pd
import re
import numpy as np


import matplotlib.pyplot as plt




pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)


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

tweets['rapido'] = tweets['text'].apply(lambda tweet: word_in_text('rapido', tweet))
tweets['normal'] = tweets['text'].apply(lambda tweet: word_in_text('normal', tweet))
tweets['lento']  = tweets['text'].apply(lambda tweet: word_in_text('lento', tweet))
tweets['caido'] = tweets['text'].apply(lambda tweet: word_in_text('caido', tweet))
tweets['malo'] = tweets['text'].apply(lambda tweet: word_in_text('malo', tweet))
tweets['bueno'] = tweets['text'].apply(lambda tweet: word_in_text('bueno', tweet))


velocit_options = ['rapido','normal','lento']
service_optiosn = ['caido','malo','bueno']

tweets_by_velocity = tweets['rapido'].value_counts()[True], tweets['normal'].value_counts()[True], tweets['lento'].value_counts()[True]


tweets_by_service = tweets['caido'].value_counts()[True], tweets['malo'].value_counts()[True], tweets['bueno'].value_counts()[True]


x_pos = list(range(len(velocit_options)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_velocity, width, alpha=1, color='g')


ax.set_ylabel('Número de tweets', fontsize=15)
ax.set_title('Velocidad: rapido vs. normal vs. lento (dato crudo)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(velocit_options)
plt.grid()



x_pos = list(range(len(velocit_options)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_service, width, alpha=1, color='g')


ax.set_ylabel('Número de tweets', fontsize=15)
ax.set_title('Servicio: caido vs. malo vs. bueno (dato crudo)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(service_optiosn)
plt.grid()





print("Velocidad del Internet: ")
print ("rapido", tweets['rapido'].value_counts()[True] ) 

print ("normal", tweets['normal'].value_counts()[True])

print ("lento", tweets['lento'].value_counts()[True])


print("Disponibilidad del servicio: ")
print ("caido", tweets['caido'].value_counts()[True])

print ("malo", tweets['malo'].value_counts()[True])

print ("bueno", tweets['bueno'].value_counts()[True])

tweets_by_lang = tweets['lang'].value_counts()




plt.show()


