"""Base core for flask app."""
from random import sample
from flask import Flask, render_template, jsonify
from util import get_neighborhood_count


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chart.html')

@app.route('/data')
def data():
    return jsonify({'results' : sample(range(1, 10), 5)})

@app.route('/booking')
def get_booking_optimal():
    return 'will return optimal price for optimal booking.'

@app.route('/neighboorhoods')
def neighboorhoods():
    return jsonify(get_neighborhood_count())



if __name__ == '__main__':
    app.run(debug=True)
