from datetime import datetime

import googlemaps

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(track=["#HACKPSUHELPLINE"])

# for temp in tweepy.Cursor(api.search, q="#HACKPSUHELPLINE", ang="en").items():
#     print(temp)

# for tweet in tweepy.Cursor(api.search, q="#pokemonleak", count=100,
#                            lang="en").items():
#     print (tweet.created_at, tweet.text)

# gmaps = googlemaps.Client(key='AIzaSyBKRd5kn3yHGCja-ao7mQcmwHBbvdgvyTM')

# # Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# # Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# print(reverse_geocode_result)

# print("-" * 20)
# # Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
# print(directions_result)
