from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('error.html', errorCode='404', errorDesc='page not found'), 404

@app.errorhandler(500)
def internalServerError(error):
    return render_template('error.html', errorCode='500', errorDesc='internal server error'), 500


if __name__ == '__main__':
    app.run(debug=True)
