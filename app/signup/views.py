from flask import render_template
from flask.ext.wtf import Form
from wtforms import StringField, DateTimeField, IntegerField, SubmitField
from wtforms.validators import Required, Email, Length
from . import signup
from .. import db

class SignupForm(Form):
	name = StringField('Name', validators=[Required()])
	email = StringField('Email', validators=[Required(), Email()])
	zipcode = IntegerField('Zip/Postal Code', validators=[Required(), Length(min=0, max=0)])
	submit = SubmitField('Signup')

@signup.route('/signup/<role>')
def signup(role):
	form = SignupForm()
	name = None
	email = None
	zipcode = None
	if form.validate_on_submit():
		name = form.name.data
		email = form.email.data
		zipcode = form.zipcode.data
		form.name.data = ''
		form.email.data = ''
		form.zipcode.data = ''
	return render_template('signup.html', form=form, name=name, email=email, zipcode=zipcode)
