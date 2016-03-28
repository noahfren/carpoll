import os
from app import create_app
from flask.ext.script import Manager, Server

app = create_app('default')
manager = Manager(app)

server = Server(host = '0.0.0.0', port=5000)
manager.add_command('runserver', server)

if __name__ == '__main__':
	manager.run()