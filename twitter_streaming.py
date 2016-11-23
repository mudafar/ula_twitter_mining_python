#Variables that contains the user credentials to access Twitter API 
consumer_key    = "CQNd6xTT1qDnJTcq3bMU6g9Z6"
consumer_secret = "4uTEkgkNmdoJGpUlBqfNJ9q6icoT9y9exMIsAaBqJhniZqxsT4"
access_token    = "16898909-ELT7jgUkJkHi3Tw8BbkHOJzBwa8hxTiHg8xcVHQBY"
access_secret   = "FAFqFvRQ6XfVkCc4LdJa0SBIXlVRPv1Up3HWLFU4dt3P5"




import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener



class MyListener(StreamListener):
    """Custom StreamListener for streaming data."""

    def on_data(self, data):
        try:
            with open("data.json", 'a') as f:
                f.write(data)
                print(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        print(status)
        return True



if __name__ == '__main__':

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    twitter_stream = Stream(auth, MyListener())
    twitter_stream.filter(track=['addpi_redula','redula'])

