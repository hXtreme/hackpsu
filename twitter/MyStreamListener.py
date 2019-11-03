import numpy as np
import tweepy

from app import db
from app import models


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.place.bounding_box.coordinates != None:
            temp = status.place.bounding_box.coordinates
            np_temp = np.array(temp)
            np_avg = np.average(np_temp, axis=1)
            t_avg_coords = np.reshape(np_avg, (2, ))
            t_lat = t_avg_coords[0]
            t_lng = t_avg_coords[1]
        t_username = status.user.screen_name
        t_message = status.text
        t_radius = 0

        user = models.Requesters.query.filter_by(username=t_username).first()
        # Check the user exists
        if user is not None:
            print("Request Exists")
        else:
            requester = models.Requesters(
                username=t_username,
                lat=t_lat,
                lng=t_lng,
                message=t_message,
                radius=t_radius,
            )
            # Insert the user in the database
            db.session.add(requester)
            db.session.commit()

        print(t_username, t_message, t_lat, t_lng, t_radius)
        print("-" * 30)
