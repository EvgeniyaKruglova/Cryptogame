import tweepy
from Cryptogameproject.Cryptogameapp.models import Profile

consumer_key = 'g6ElvnvtQK6OFw4IMKymliz4H'
consumer_secret = 'dOlbS7hje8f5fcZrUAVsrzdBDESlS8Lz9YBWIMksV2r575gUkx'
access_token = '1726658056551907329-u4FqBPcaWD9SuVIbZaNeB6hunCUOFA'
access_token_secret = 'z3dTyVMCqz50Xry7zRqRnt4gHrhno1Fe9WovL3O0CywI9'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

username = Profile.twitter_username
try:
    user = api.get_user(screen_name=username)
    user_id = user.id
    print(f'User ID for {username} is: {user_id}')
except tweepy.error.TweepError as e:
    print(f'Error: {e}')
