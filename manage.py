#!/usr/bin/env python
import os
from app import create_app, db
from app.models import Country, City, Type, Museum, Period
from flask.ext.script import Manager, Shell

app = create_app('development')
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, Country=Country, City=City, Type=Type, Museum=Museum, Period=Period)
manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
