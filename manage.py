from flask.ext.script import Manager, prompt_bool, Shell, Server
from termcolor import colored
from twitter.TwitterWorker import *
from app import app, db, models
import sys

print("Test-1")

manager = Manager(app)


def make_shell_context():
    return dict(app=app)


@manager.command
def initdb():
    ''' Create the SQL database. '''
    db.create_all()
    print(colored('The SQL database has been created', 'green'))


@manager.command
def dropdb():
    ''' Delete the SQL database. '''
    if prompt_bool('Are you sure you want to lose all your SQL data?'):
        db.drop_all()
        print(colored('The SQL database has been deleted', 'green'))


manager.add_command('runserver', Server())
manager.add_command('shell', Shell(make_context=make_shell_context))

twitter_allowed = ['runserver']

if __name__ == '__main__':

    print("*" * 50)
    if len(sys.argv) > 1:
        if sys.argv[1] in twitter_allowed:
            worker = TwitterWorker()
            worker.daemon = True
            worker.start()
        manager.run()
