import sys

from flask.ext.script import Manager
from flask.ext.script import prompt_bool
from flask.ext.script import Server
from flask.ext.script import Shell
from termcolor import colored

from app import app
from app import db
from app import models
from twitter.TwitterWorker import *

manager = Manager(app)


def make_shell_context():
    return dict(app=app)


@manager.command
def initdb():
    """ Create the SQL database. """
    db.create_all()
    print(colored("The SQL database has been created", "green"))


@manager.command
def dropdb():
    """ Delete the SQL database. """
    if prompt_bool("Are you sure you want to lose all your SQL data?"):
        db.drop_all()
        print(colored("The SQL database has been deleted", "green"))


manager.add_command("runserver", Server())
manager.add_command("shell", Shell(make_context=make_shell_context))

twitter_allowed = ["runserver"]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] in twitter_allowed:
            worker = TwitterWorker()
            worker.start()
        manager.run()
