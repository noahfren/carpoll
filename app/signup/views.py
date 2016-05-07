from flask import render_template, redirect, url_for
from . import signup
from .. import db
from ..models import User, Driver, Rider
from .forms import DriverForm, RiderForm

@signup.route('/driver', methods=['GET', 'POST'])
def driver_signup():
	form = DriverForm()
	if form.validate_on_submit():
		driver = Driver(name=form.name.data,
			email=form.email.data,
			zipcode=form.zipcode.data,
			num_passengers=form.num_passengers.data)
		db.session.add(driver)
		return redirect(url_for('index'))
	return render_template('signup.html', form=form)

@signup.route('/rider', methods=['GET', 'POST'])
def rider_signup():
	form = RiderForm()
	if form.validate_on_submit():
		rider = Rider(name=form.name.data,
			email=form.email.data,
			zipcode=form.zipcode.data)
		db.session.add(rider)
		return redirect(url_for('index'))
	return render_template('signup.html', form=form)