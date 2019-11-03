from threading import Thread

import tweepy

from twitter.MyStreamListener import MyStreamListener


class TwitterWorker(Thread):
    def __init__(self):
        Thread.__init__(self)
        CONSUMER_KEY = "IwZZeJHjLXq55ewwQwD0SogHU"
        CONSUMER_SECRET = "80kELQhDGNvLNFfNZ7qliIbzAoA3tsgQaAEnnMNWKIr6uMN6Ri"
        ACCESS_TOKEN = "857838183224139776-1HrWNTQk8pywtozedEAou6tr7CkB4Uu"
        ACCESS_TOKEN_SECRET = "NkP6s5UZuoBmDSW31mhTzudNSQKpvxwwuE3pcWYcytWgU"
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)

    def run(self):
        streamListener = MyStreamListener()
        self.stream = tweepy.Stream(auth=self.api.auth, listener=streamListener)
        self.stream.filter(track=["#HACKPSUHELPLINE"])


if __name__ == "__main__":
    print("Starting Stream..")
    tw = TwitterWorker()
    tw.streaming()
