import os
from flask import Flask, render_template
from flask.ext.script import Manager
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

base = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

manager = Manager(app)
Bootstrap(app)

@app.route('/')
def index():
    countries = Country.query.all()
    return render_template('index.html', countries=countries)

@app.route('/<cityname>')
def city(cityname):
    city = City.query.filter(City.name.ilike(cityname)).first()
    return render_template('city.html', city=city)

class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    flagURL = db.Column(db.String(20), unique=True)
    cities = db.relationship('City', backref='country', lazy='dynamic')

    def __repr__(self):
        return '<Country {0}>'.format(self.name)

class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))

    def __repr__(self):
        return '<City {0}>'.format(self.name)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('error.html', errorCode='404', errorDesc='page not found'), 404

@app.errorhandler(500)
def internalServerError(error):
    return render_template('error.html', errorCode='500', errorDesc='internal server error'), 500


if __name__ == '__main__':
    manager.run()
