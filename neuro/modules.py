from datetime import datetime
import string
from random import choices
from neuro import db



class UserLink(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    original_url = db.Column(db.String(2000))
    short_url = db.Column(db.String(7),unique=True,nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_link()
        #self.custom_url = self.generate_custom_url()
        #self.custom_name = se lf.generate_custom_url()

    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=7))

        link = self.query.filter_by(short_url=short_url).first()

        if link:
            return self.generate_short_link()
        return short_url


class Links(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    links = db.Column(db.String(2000))
    titles = db.Column(db.String(2000))