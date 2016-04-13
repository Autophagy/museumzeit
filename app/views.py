from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import Country, City
from . import main

@main.route('/')
def index():
    countries = Country.query.all()
    return render_template('index.html', countries=countries)

@app.route('/<cityname>')
def city(cityname):
    city = City.query.filter(City.name.ilike(cityname)).first()
    return render_template('city.html', city=city)
