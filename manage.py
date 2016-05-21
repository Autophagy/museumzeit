#!/usr/bin/env python
import os
from app import create_app, db
from app.models import Country, City, Type, Museum, Period
from flask.ext.script import Manager, Shell
from werkzeug.contrib.profiler import ProfilerMiddleware

app = create_app('development')
manager = Manager(app)

COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()

def make_shell_context():
    return dict(app=app, db=db, Country=Country, City=City, Type=Type, Museum=Museum, Period=Period)
manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def test(coverage=False):
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        import sys
        os.environ['FLASK_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv)

    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML report: file://{}/index.html'.format(covdir))
        COV.erase()

@manager.command
def profile(length=25, profile_dir=None):
    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length], profile_dir=profile_dir)
    app.run()

@manager.command
def deploy():
    import finaldata as fd
    db.drop_all()
    db.create_all()

    Country.insertCountries(fd.getCountries())
    City.insertCities(fd.getCities())
    Type.insertTypes(fd.getTypes())
    Museum.insertMuseums(fd.getMuseums())
    Period.insertPeriods(fd.getPeriods())

if __name__ == '__main__':
    manager.run()
