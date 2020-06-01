import tweepy
import time

auth = tweepy.OAuthHandler('', '')
auth.set_access_token("", '')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'Arknights'

for tweet in tweepy.Cursor(api.search, search).items(5):
	try:
		print('Tweet Liked')
		tweet.favorite()
		time.sleep(10)
	except StopIteration:
		break
