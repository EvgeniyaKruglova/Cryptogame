import tweepy
import requests
import json
from .models import Profile

consumer_key = 'g6ElvnvtQK6OFw4IMKymliz4H'
consumer_secret = 'dOlbS7hje8f5fcZrUAVsrzdBDESlS8Lz9YBWIMksV2r575gUkx'
access_token = '1726658056551907329-u4FqBPcaWD9SuVIbZaNeB6hunCUOFA'
access_token_secret = 'z3dTyVMCqz50Xry7zRqRnt4gHrhno1Fe9WovL3O0CywI9'
bearer_token = "AAAAAAAAAAAAAAAAAAAAANB9rAEAAAAAF9GbfFN7VNCdR8fHyXUnPUjCRdM%3DGRMfXGSIQmWjrcVNNCouH3izxoTROfQ8jJfsPgZYZ1KV0SdyrH"

def twitter_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api



# функция для получения ID пользователя Twitter по его username
def get_twitter_user_id(username):
    # формируем URL для запроса к API Twitter
    url = "https://api.twitter.com/1.1/users/show.json?screen_name=" + str(username)
    # делаем запрос к API Twitter
    response = requests.get(url, auth=(consumer_key, consumer_secret, access_token, access_token_secret))
    # получаем JSON-объект, содержащий информацию о пользователе
    user_data = json.loads(response.text)
    # извлекаем ID пользователя из JSON-объекта
    user_id = user_data['id']
    return user_id

#поиск твитов по ключевому слову
def search_twitter(query):
    api = twitter_api()
    response = api.search_tweets(q=query)
    tweets = json.dumps(response)
    return tweets


# tweets = search_twitter('python')
#
# for tweet in tweets:
#     print(tweet.text)

