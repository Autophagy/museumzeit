from flask import Flask
app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return '<h1>museumzeit</h1>'

if __name__ == '__main__':
    app.run(debug=True)
