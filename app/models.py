from . import db
from sqlalchemy.ext.hybrid import hybrid_method

class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    flagURL = db.Column(db.String(20), unique=True)
    cities = db.relationship('City', backref='country', lazy='dynamic')

    @staticmethod
    def insertCountries(countries):
        for c in countries:
            country = Country.query.filter_by(name=c).first()
            if country is None:
                country = Country(name=c)
            country.flagURL = countries[c][0]
            db.session.add(country)
        db.session.commit()

    def __repr__(self):
        return '<Country {0}>'.format(self.name)

class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64), unique=True)
    timezone = db.Column(db.String(64))
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    museums = db.relationship('Museum', backref='city', lazy='dynamic')

    @staticmethod
    def insertCities(cities):
        for c in cities:
            city = City.query.filter_by(name=c).first()
            if city is None:
                city = City(name=c)
            city.timezone = cities[c][0]
            city.country = Country.query.filter_by(name=cities[c][1]).first()
            db.session.add(city)
        db.session.commit()

    def __repr__(self):
        return '<City {0}>'.format(self.name)

class Type(db.Model):
    __tablename__ = 'types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    iconURL = db.Column(db.String(20), unique=True)
    museums = db.relationship('Museum', backref='type', lazy='dynamic')

    @staticmethod
    def insertTypes(types):
        for t in types:
            type = Type.query.filter_by(name=t).first()
            if type is None:
                type = Type(name=t)
            type.iconURL = types[t][0]
            db.session.add(type)
        db.session.commit()

    def __repr__(self):
        return '<Type {0}>'.format(self.name)

class Museum(db.Model):
    __tablename__ = 'museums'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64), unique=True)
    description = db.Column(db.UnicodeText)
    website = db.Column(db.String(64))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'))
    periods = db.relationship('Period', backref='museum', lazy='dynamic')

    free = None
    closed = None
    validPeriods = None

    @staticmethod
    def insertMuseums(museums):
        for m in museums:
            museum = Museum.query.filter_by(name=m).first()
            if museum is None:
                museum = Museum(name=m)
            museum.description = museums[m][0]
            museum.website = museums[m][1]
            museum.latitude = museums[m][2]
            museum.longitude = museums[m][3]
            museum.city = City.query.filter_by(name=museums[m][4]).first()
            museum.type = Type.query.filter_by(name=museums[m][5]).first()
            db.session.add(museum)
        db.session.commit()

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

    @staticmethod
    def insertPeriods(periods):
        Period.query.delete()
        for p, item in enumerate(periods):
            period = Period()
            period.open = periods[p][0]
            period.openTime = periods[p][1]
            period.closedTime = periods[p][2]
            period.weekday = periods[p][3]
            period.free = periods[p][4]
            period.museum = Museum.query.filter_by(name=periods[p][5]).first()
            db.session.add(period)
        db.session.commit()

    def __repr__(self):
        return '<Period [{0}] - [{1}] for museum {2}>'.format(self.openTime,self.closedTime, self.museum_id)
