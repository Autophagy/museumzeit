from . import db
from sqlalchemy.ext.hybrid import hybrid_method

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

    @hybrid_method
    def isFree(self, date):
        periods = self.getValidPeriods(date)
        return reduce(lambda a,b: a or b, map((lambda x: x.free), periods))

    @hybrid_method
    def isClosed(self, date):
        periods = self.getValidPeriods(date)
        return reduce(lambda a,b: a or b, map((lambda x: not x.open), periods))

    @hybrid_method
    def getValidPeriods(self, date):
        # Return periods according to the following priority:
        # 1. Records with between dates and a specific day.
        # 2. Records with no between dates, but a specific day.
        # 3. Records with between dates, but no day.
        # 4. Records with no between dates and no day.

        day = date.weekday()

        periods = self.periods.filter(Period.validFrom <= date, Period.validTo >= date, Period.weekday == day).count()
        if periods > 0:
            return self.periods.filter(Period.validFrom <= date, Period.validTo >= date, Period.weekday == day).all()

        periods = self.periods.filter(Period.weekday == day).count()
        if periods > 0:
            return self.periods.filter(Period.weekday == day).all()

        periods = self.periods.filter(Period.validFrom <= date, Period.validTo >= date).count()
        if periods > 0:
            return self.periods.filter(Period.validFrom <= date, Period.validTo >= date).count().all()

        return self.periods

class Period(db.Model):
    __tablename__ = 'periods'
    id = db.Column(db.Integer, primary_key=True)
    validFrom = db.Column(db.Date, nullable=True)
    validTo = db.Column(db.Date, nullable=True)
    weekday = db.Column(db.Integer, nullable=True)
    open = db.Column(db.Boolean)
    openTime = db.Column(db.Time, nullable=True)
    closedTime = db.Column(db.Time, nullable=True)
    free = db.Column(db.Boolean)
    museum_id = db.Column(db.Integer, db.ForeignKey('museums.id'))

    def __repr__(self):
        return '<Period [{0}] - [{1}] for museum {2}>'.format(self.openTime,self.closedTime, self.museum_id)
