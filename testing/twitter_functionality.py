import tweepy
from twitter_stream import MyStreamListener


def oauth_authenticate():
    CONSUMER_KEY = "IwZZeJHjLXq55ewwQwD0SogHU"
    CONSUMER_SECRET = "80kELQhDGNvLNFfNZ7qliIbzAoA3tsgQaAEnnMNWKIr6uMN6Ri"
    ACCESS_TOKEN = "857838183224139776-1HrWNTQk8pywtozedEAou6tr7CkB4Uu"
    ACCESS_TOKEN_SECRET = "NkP6s5UZuoBmDSW31mhTzudNSQKpvxwwuE3pcWYcytWgU"
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    return api


def streaming():
    api = oauth_authenticate()
    streamListener = MyStreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=streamListener)
    stream.filter(track=["#HACKPSUHELPLINE"])


if __name__ == "__main__":
    print("wanting to stream")
    streaming()
    print("EXITING")
