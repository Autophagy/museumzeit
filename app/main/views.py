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
    city = City.query.filter(City.name.ilike(cityname)).first()

    # If no city is found, throw a 404 error
    if city == None:
        abort(404)

    return render_template('city.html', city=city)
