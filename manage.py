#!/usr/bin/env python
import os
from app import create_app, db
from app.models import Country, City, Type, Museum, Period
from flask.ext.script import Manager, Shell
from werkzeug.contrib.profiler import ProfilerMiddleware

app = create_app('development')
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, Country=Country, City=City, Type=Type, Museum=Museum, Period=Period)
manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
