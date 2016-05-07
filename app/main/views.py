from flask import render_template, request
from . import main
from .. import db, signup

@main.route('/')
def index():
	return render_template('home.html')
