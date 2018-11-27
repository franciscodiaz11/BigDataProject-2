#Import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#Variables that contains the user credentials to access Twitter API 
access_token = "1007363226336624641-UkflVfa7vA82ANoJqPmf6MKmum5Rdh"
access_token_secret = "aAAZedbVeP5rSpNGeZvnaMzyxihSfvrNcQLWin5Yyyt6n"
consumer_key = "GAGeGFWOxoUIhzOi1s0gABs5W"
consumer_secret = "BFsTs3NKfw48GStC5ZcHQQsjFkfbDK01Ok9jXl6N0MLbLA3VYo"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    api = tweepy.API(auth)
    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['python', 'javascript', 'ruby'])
    stream.sample()
    #for status in tweepy.Cursor(api.home_timeline).items(10):
        #process a single status
        #print(status.text)
   #stream.filter(languages=["en"])