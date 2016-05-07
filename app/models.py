from . import db
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
	"""SUPER-CLASS REPRESENTATION OF ALL USERS"""
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	email = db.Column(db.String(50), unique=True)
	zipcode = db.Column(db.String(5), index=True)
	user_type = db.Column(db.String(10))
	__mapper_args__ = {'polymorphic_identity': 'user',
		'polymorphic_on' : user_type}


class Driver(User):
	"""REPRESENTATION OF VOLUNTEER DRIVERS"""
	id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
	__mapper_args__ = {'polymorphic_identity' : 'driver'}
	num_passengers = db.Column(db.Integer)
	passengers = db.relationship('Rider', backref='driver')



class Rider(User):
	"""REPRESENTATION OF RIDERS"""
	id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
	__mapper_args__ = {'polymorphic_identity' : 'rider'}
	has_ride = db.Column(db.Boolean, default=False)
	driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable=True)

