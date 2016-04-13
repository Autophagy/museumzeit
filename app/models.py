from . import db

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
