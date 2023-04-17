from sqlalchemy_serializer import SerializerMixin

from config import db

class Fan(db.Model):
    __tablename__ = 'fans'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    dob = db.Column(db.Date, nullable=False)

    tickets = db.relationship('Ticket', backref='fan')

class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    tickets = db.relationship('Ticket', backref='venue')


class Ticket(db.Model):
    __tablename__ = 'concerts'

    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String, nullable=False)
    age_restriction = db.Column(db.Boolean, nullable=False, default=False)

    fan_id = db.Column(db.Integer, db.ForeignKey('fans.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)

