from sqlalchemy.ext.hybrid import hybrid_property
from flask.ext.login import UserMixin

from app import db, bcrypt


class Requesters(db.Model, UserMixin):

    ''' A requesters who needs help '''

    __tablename__ = 'requesters'

    user_name = db.Column(db.String, primary_key=True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    message = db.Column(db.String)


class Responder(db.Model, UserMixin):

    ''' A responder who has an account on the website. '''

    __tablename__ = 'responders'

    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String, primary_key=True)
    confirmation = db.Column(db.Boolean)
    _password = db.Column(db.String)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def check_password(self, plaintext):
        return (self.password == plaintext)

    def get_id(self):
        return self.email

