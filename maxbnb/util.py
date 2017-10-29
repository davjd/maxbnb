"""Methods for analyzing the data."""
from operator import itemgetter
import csv


def get_neighborhood_dict(val):
    neighbourhoods = {}
    with open('data/neighbourhoods.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            neighbourhoods[row['neighbourhood']] = val
    return neighbourhoods


def get_neighborhood_count():
    """returns a dictionary of the neighborhoods and the number of listings."""
    neighbourhoods = get_neighborhood_dict(0)
    with open('data/listings.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            neighbourhoods[row['neighbourhood_cleansed']] += 1
    return neighbourhoods

def get_most_positive_reviews(rating_type):
    with open('data/listings.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        neighborhoods = get_neighborhood_dict([0, 0])
        row_rates = ['review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness',\
        'review_scores_checkin', 'review_scores_communication', 'review_scores_location', \
        'review_scores_value']
        max_ratings = []

        if not rating_type in row_rates:
            return max_ratings
        for row in reader:
            if not row[rating_type] == '':
                neighborhoods[row['neighbourhood_cleansed']][0] += 1
                neighborhoods[row['neighbourhood_cleansed']][1] += int(row[rating_type])
        for neighborhood, ratings in neighborhoods.items():
            rating_avg = ratings[1] / float(ratings[0])
            print rating_avg
            max_ratings.append([neighborhood, rating_avg])
        #max_ratings.sort(key=itemgetter(1))
        return max_ratings

max_ratings = get_most_positive_reviews('review_scores_rating')
"""for ratings in max_ratings:
    print ratings[0], ': ', ratings[1]"""


"""def get_most_reviews():
    #neighborhoods = get_neighborhood_dict([0, 0] * 7)
    with open('data/listings.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        row_rates = ['review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness',\
        'review_scores_checkin', 'review_scores_communication', 'review_scores_location', \
        'review_scores_value']
        for row in reader:
            room_ratings = [row['neighbourhood_cleansed'], [0] * 7]
            for ctr, rate_type in enumerate(row_rates):
                if row[rate_type] == '':
                    rate = -1
                else:
                    rate = float(row[rate_type])
                room_ratings[1][ctr] = rate"""
           