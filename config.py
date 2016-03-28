import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = 'sadkjhfkdjshgeytertgfasdgdfahgfhds'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True

	@staticmethod
	def init_app(app):
		pass

class Development(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/noahfrenkel/Desktop/carpoll_flask/db.sqlite'

class Production(Config):
	pass

config = {
	'development' : Development,
	'production' : Production,
	'default' : Development 
}