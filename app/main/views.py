import datetime
from flask import render_template, session, redirect, url_for, current_app, abort
from .. import db
from ..models import Country, City
from . import main

@main.route('/')
def index():
    countries = Country.query.all()
    return render_template('index.html', countries=countries)

@main.route('/<cityname>')
def city(cityname):
    # No date provided, use today
    date = datetime.datetime.now()
    return cityWithDate(cityname, date.strftime('%d-%m-%Y'))

@main.route('/<cityname>/<date>')
def cityWithDate(cityname, date):

    try:
        formattedDate = datetime.datetime.strptime(date, '%d-%m-%Y')
    except ValueError:
        abort(404)

    city = City.query.filter(City.name.ilike(cityname)).first()

    # If no city is found, throw a 404 error
    if city == None:
        abort(404)

    museumPeriods = [x for f in map((lambda x: x.getValidPeriods(formattedDate)), city.museums) for x in f]

    earliestTime = reduce(lambda a,b: a if (a < b) else b, map((lambda x: x.openTime), museumPeriods))
    earliestTime = earliestTime.hour + 1 if earliestTime.minute > 30 else earliestTime.hour

    latestTime = reduce(lambda a,b: a if (a > b) else b, map((lambda x: x.closedTime), museumPeriods))
    latestTime = latestTime.hour + 1 if latestTime.minute > 30 else latestTime.hour

    return render_template('city.html', city=city, date=formattedDate, earliestTime=earliestTime, latestTime=latestTime)
