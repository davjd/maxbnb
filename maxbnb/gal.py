"""Methods that'll create the svg graph files."""
import pygal
from pygal.style import TurquoiseStyle
from pygal.style import NeonStyle
from pygal.style import DarkStyle
from util import get_neighborhood_count, get_most_avaliable, get_most_expensive, get_neighborhoods, get_overall_reviews


def generate_graphs():
    """generates all graphs for the three trends from the dataset."""
    #generate graph of number of listings in each neighborhood.
    neighborhood_count_chart = pygal.Pie(style=DarkStyle)
    neighborhood_count_chart.title = 'The number of listings each neighborhood has'
    neighborhood_count = get_neighborhood_count()
    for k, val in neighborhood_count.items():
        neighborhood_count_chart.add(k, val)
    neighborhood_count_chart.render_to_file('static/assets/neighborhood_countgraph.svg')

    #generate graph of average price for each neighborhood.
    most_expensive_chart = pygal.HorizontalBar(legend_box_size=4, style=NeonStyle)
    most_expensive_chart.title = 'The average night cost for each neighborhood ($)'
    most_expensive = get_most_expensive()
    for neighborhood in most_expensive:
        most_expensive_chart.add(neighborhood[0], float("{0:.2f}".format(neighborhood[1])))
    most_expensive_chart.render_to_file('static/assets/most_expensivegraph.svg')

    #generate graph of average availability_365 in each neighborhood.
    most_avaliable_chart = pygal.Bar(legend_box_size=4, style=TurquoiseStyle)
    most_avaliable_chart.title = 'The average availability in the next 365 days of each neighborhood (days)'
    most_avaliable = get_most_avaliable()
    for neighborhood in most_avaliable:
        most_avaliable_chart.add(neighborhood[0], [{'value': neighborhood[1]}])
    most_avaliable_chart.render_to_file('static/assets/most_availablegraph.svg')

    #generate graph of sorted reviews.
    reviews_chart = pygal.HorizontalBar(legend_box_size=4, style=NeonStyle)
    reviews_chart.title = 'Average reviews of neighborhoods'
    reviews = get_overall_reviews()
    for neighborhood in reviews:
        reviews_chart.add(neighborhood[0], float("{0:.2f}".format(neighborhood[1])))
    reviews_chart.render_to_file('static/assets/reviewsgraph.svg')

generate_graphs()
