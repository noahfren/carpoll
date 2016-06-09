
### Code Sample 1: 
### Model Definitions for carpoll database in python using flask and SQlAlchemy
### Driver and Rider both inherit from User using joined table inheritance

from . import db
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
	"""BASE CLASS FOR USERS OF CARPOLL"""
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	email = db.Column(db.String(50), unique=True)
	zipcode = db.Column(db.String(10), index=True)
	type = db.Column(db.String(10))
	__mapper_args__ = {'polymorphic_identity' : 'user',
	'polymorphic_on' : type}


class Driver(User):
	"""REPRESENTATION OF VOLUNTEER DRIVERS - INHERITS FROM USER"""
	__tablename__ = 'drivers'
	__mapper_args__ = {'polymorphic_identity' : 'driver'}
	id = db.Column(db.Integer, db.ForeignKey(User.id), primary_key=True)
	num_passengers = db.Column(db.Integer, default=0)
	max_passengers = db.Column(db.Integer)
	passengers = db.relationship('Rider', backref='driver')

	def __repr__(self):
		return '<Driver %r>' % self.name

	def find_riders(self):
		new_passengers =  Rider.query.filter_by(zipcode=self.zipcode).filter_by(has_ride=False).all()
		for i in range(0, min(self.max_passengers, len(new_passengers))):
			new_passengers[i].driver_id = self.id
			new_passengers[i].has_ride = True
			self.num_passengers += 1
		return


class Rider(User):
	"""REPRESENTATION OF RIDERS - INHERITS FROM USER"""
	__tablename__ = 'riders'
	__mapper_args__ = {'polymorphic_identity' : 'rider'}
	id = db.Column(db.Integer, db.ForeignKey(User.id), primary_key=True)
	has_ride = db.Column(db.Boolean, default=False)
	driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable=True)

	def __repr__(self):
		return '<Rider %r>' % self.name

	def find_driver(self):
		if self.has_ride:
			return

		new_driver = Driver.query\
		.filter_by(zipcode=self.zipcode).filter(Driver.num_passengers<Driver.max_passengers)\
		.order_by(Driver.num_passengers).first()
		new_driver.num_passengers += 1
		self.has_driver = True
		return


