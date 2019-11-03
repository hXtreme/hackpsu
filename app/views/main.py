from flask import render_template, jsonify
from app import app
from app import models, db
import json
import random


class User:
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Map')


@app.route('/nav')
def nav():
    return render_template('nav.html', title='Navigation')


@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/api/getInNeedRequester', methods=['GET'])
# retrieves/adds polls from/to the database
def api_getInNeedRequester():

    requesters = models.Requesters.query.all()

    requester_list = list()
    for temp in requesters:
        requester_list.append({'username': temp.username, 'lat': temp.lat, 'lng': temp.lng, 'message': temp.message, 'radius': temp.radius, 'matched': temp.matched})
    print(requester_list)
    return json.dumps(requester_list)
