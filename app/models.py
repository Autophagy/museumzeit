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

    free = None
    closed = None
    validPeriods = None

    def __repr__(self):
        return '<Museum {0}>'.format(self.name)

    @hybrid_method
    def isFree(self, date):
        if self.free is not None:
            return self.free
        else:
            periods = self.getValidPeriods(date)
            self.free = reduce(lambda a,b: a or b, map((lambda x: x.free), periods))
            return self.free

    @hybrid_method
    def isClosed(self, date):
        if self.closed is not None:
            return self.closed
        else:
            periods = self.getValidPeriods(date)
            self.closed = reduce(lambda a,b: a or b, map((lambda x: not x.open), periods))
            return self.closed

    @hybrid_method
    def getValidPeriods(self, date):
        # Return periods according to the following priority:
        # A. Records with between dates and a specific day.
        # B. Records with no between dates, but a specific day.
        # C. Records with between dates, but no day.
        # D. Records with no between dates and no day.

        if self.validPeriods is not None:
            return self.validPeriods
        else:

            day = date.weekday()

            periods = self.periods.filter(Period.validFrom <= date, Period.validTo >= date, Period.weekday == day).all()
            if periods != []:
                self.validPeriods = periods
                return self.validPeriods

            periods = self.periods.filter(Period.weekday == day).all()
            if periods != []:
                self.validPeriods = periods
                return self.validPeriods

            periods = self.periods.filter(Period.validFrom <= date, Period.validTo >= date).all()
            if periods != []:
                self.validPeriods = periods
                return self.validPeriods

            self.validPeriods = self.periods.filter(Period.validFrom == None, Period.validTo == None, Period.weekday == None).all()
            return self.validPeriods

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
