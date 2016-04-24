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
    timezone = db.Column(db.String(64))
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    museums = db.relationship('Museum', backref='city', lazy='dynamic')

    def __repr__(self):
        return '<City {0}>'.format(self.name)

class Type(db.Model):
    __tablename__ = 'types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    iconURL = db.Column(db.String(20), unique=True)
    museums = db.relationship('Museum', backref='type', lazy='dynamic')

    def __repr__(self):
        return '<Type {0}>'.format(self.name)

class Museum(db.Model):
    __tablename__ = 'museums'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.Text)
    website = db.Column(db.String(64))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'))
    periods = db.relationship('Period', backref='museum', lazy='dynamic')

    def __repr__(self):
        return '<Museum {0}>'.format(self.name)

class Period(db.Model):
    __tablename__ = 'periods'
    id = db.Column(db.Integer, primary_key=True)
    validFrom = db.Column(db.Date, nullable=True)
    validTo = db.Column(db.Date, nullable=True)
    openTime = db.Column(db.Time)
    closedTime = db.Column(db.Time)
    free = db.Column(db.Boolean)
    museum_id = db.Column(db.Integer, db.ForeignKey('museums.id'))

    def __repr__(self):
        return '<Period {0} [{1}] - {2} [{3}] for museum {4}>'.format(self.validFrom, self.openTime, self.ValidTo, self.closedTime, self.museum_id)
