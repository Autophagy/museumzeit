from flask import render_template
from . import main

@main.errorhandler(404)
def pageNotFound(error):
    return render_template('error.html', errorCode='404', errorDesc='page not found'), 404

@main.errorhandler(500)
def internalServerError(error):
    return render_template('error.html', errorCode='500', errorDesc='internal server error'), 500
