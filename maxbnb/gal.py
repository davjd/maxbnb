"""Methods that'll create the svg graph files."""
import pygal
from util import get_neighborhood_count, get_most_avaliable, get_most_expensive, get_neighborhoods


def generate_graphs():
    """generates all graphs for the three trends from the dataset."""
    #generate graph of number of listings in each neighborhood.
    neighborhood_count_chart = pygal.Pie()
    neighborhood_count_chart.title = 'The number of listings each neighborhood has'
    neighborhood_count = get_neighborhood_count()
    for k, val in neighborhood_count.items():
        neighborhood_count_chart.add(k, val)
    neighborhood_count_chart.render_to_file('static/assets/neighborhood_count_chart.svg')

    #generate graph of average availability_365 in each neighborhood.
    most_avaliable_chart = pygal.Line(x_label_rotation=20)
    most_avaliable_chart.title = 'The average availability in the next 365 days of each neighborhood'
    most_avaliable = get_most_avaliable()
    most_avaliable_chart.x_labels = [item[0] for item in most_avaliable]
    for k, val in most_avaliable.items():
        most_avaliable_chart.add(k, [val])
    most_avaliable_chart.render_to_file('static/assets/most_expensive_chart.svg')
