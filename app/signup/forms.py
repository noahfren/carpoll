from flask.ext.wtf import Form
from wtforms import StringField, DateTimeField, IntegerField, SubmitField
from wtforms.validators import Required, Email
from ..models import Driver, Rider

class SignupForm(Form):
	"""USER SIGN-UP FORM SUPER-CLASS""" 
	name = StringField('Name', validators=[Required()])
	email = StringField('Email', validators=[Required(), Email()])
	zipcode = StringField('Zip/Postal Code', validators=[Required()])

class DriverForm(SignupForm):
	"""DRIVER SIGN-UP FORM"""
	max_passengers = IntegerField('Number of Passengers', validators=[Required()])
	submit = SubmitField('Signup')

	def validate_email(self, field):
		if Driver.query.filter_by(email=field.data).first():
			raise ValidationError('We\'re sorry, this Email is already in use.')

class RiderForm(SignupForm):
	"""RIDER SIGN-UP FORM"""
	submit = SubmitField('Signup')

	def validate_email(self, field):
		if Rider.query.filter_by(email=field.data).first():
			raise ValidationError('We\'re sorry, this Email is already in use.')
