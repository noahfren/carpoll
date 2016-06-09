from flask import render_template, redirect, url_for
from . import signup
from .. import db
from ..models import Driver, Rider
from .forms import DriverForm, RiderForm

@signup.route('/driver', methods=['GET', 'POST'])
def driver_signup():
	form = DriverForm()
	if form.validate_on_submit():
		driver = Driver(name=form.name.data,
			email=form.email.data,
			zipcode=form.zipcode.data,
			type='driver',
			max_passengers=form.max_passengers.data)
		db.session.add(driver)
		driver.find_riders()
		db.session.commit()
		return redirect(url_for('main.index'))
	return render_template('signup.html', form=form)

@signup.route('/rider', methods=['GET', 'POST'])
def rider_signup():
	form = RiderForm()
	if form.validate_on_submit():
		rider = Rider(name=form.name.data,
			email=form.email.data,
			zipcode=form.zipcode.data,
			type='rider')
		db.session.add(rider)
		rider.find_drivers()
		db.session.commit()
		return redirect(url_for('main.index'))
	return render_template('signup.html', form=form)