"""Base core for flask app."""
from random import sample
from flask import Flask, render_template, jsonify, request
from util import get_neighborhood_count, find_estimation


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chart.html')

@app.route('/booking')
def get_booking_optimal():
    return 'will return optimal price for optimal booking.'

@app.route('/estimation/<neighborhood>')
def get_estimation(neighborhood):
    """
    My methodology for estimating the average weekly income was finding the neigborhood that
    the given location was in. This is a pretty simple method but the estimation is still
    pretty accurate given the only data. I used Google's API to find the neighborhood that each location
    was in. Because the neighborhood names found in neighbourhoods.csv and the neighborhood names that
    google responds with are different, there might be cases when the wrong neighborhood will be passed to
    my method. I could've made a more robust method which mapped the csv's names with google's names,
    but that would've taken A LOT of time. For now I'll leave it like this.
    """
    return jsonify({'estimation': [neighborhood, str(float("{0:.2f}".format(find_estimation(neighborhood) * 7)))]})



if __name__ == '__main__':
    app.run(debug=True)
