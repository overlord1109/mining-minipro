import tweepy
import base64

"""def paginate(iterable, page_size):
    while True:
        i1, i2 = itertools.tee(iterable)
        iterable, page = (itertools.islice(i1, page_size, None),
                list(itertools.islice(i2, page_size)))
        if len(page) == 0:
            break
        yield page"""

f=open('tolkien.txt', 'r')

consumer_key=f.readline().rstrip('\n')

#print(consumer_key)

consumer_secret=f.readline().rstrip('\n')

#print(consumer_secret)


access_token=f.readline().rstrip('\n')
access_token_secret=f.readline().rstrip('\n')

#print(access_token)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#   print(tweet.text)

user = api.get_user('realdonaldtrump')
print(user.screen_name)
print("Follower count:"+str(user.followers_count))

stuff=api.user_timeline(screen_name = user.screen_name, count = 20, include_rts = True)

for status in stuff:
	print(status.text+'\n')
"""
for block in tweepy.Cursor(api.followers_ids, 'realdonaldtrump').items():
	print(block)


for status in tweepy.Cursor(api.user_timeline(screen_name='realdonaldtrump', include_rts=True)).items():
	print(status)
"""
