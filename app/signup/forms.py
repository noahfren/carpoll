from flask.ext.wtf import Form
from wtforms import StringField, DateTimeField, IntegerField, SubmitField
from wtforms.validators import Required, Email, Length
from ..models import User

class SignupForm(Form):
	"""USER SIGN-UP FORM SUPER-CLASS""" 
	name = StringField('Name', validators=[Required()])
	email = StringField('Email', validators=[Required(), Email()])
	zipcode = IntegerField('Zip/Postal Code', validators=[Required(), Length(min=0, max=100000)])
	

	"""def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('We\'re sorry, this Email is already in use.')"""

class DriverForm(SignupForm):
	"""DRIVER SIGN-UP FORM"""
	num_passengers = IntegerField('Number of Passengers', validators=[Required(), Length(min=1, max=7)])
	submit = SubmitField('Signup')

class RiderForm(SignupForm):
	"""RIDER SIGN-UP FORM"""
	submit = SubmitField('Signup')
