"""Methods that'll create the svg files."""
import pygal
from util import get_neighborhood_count

line_chart = pygal.HorizontalBar()
line_chart.title = 'Listings in each neighborhood'

neighborhoods = get_neighborhood_count()
for key, value in neighborhoods.items():
    line_chart.add(key, value)
line_chart.render_to_file('static/assets/h.svg')
