"""Methods for analyzing the data."""
from operator import itemgetter
import csv
import io

def get_neighborhoods():
    """returns array with all the names of the neighborhoods."""
    neighbourhoods = []
    with open('data/neighbourhoods.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            neighbourhoods.append(row['neighbourhood'])
    return neighbourhoods

def get_neighborhood_dict():
    """returns dictionary with each neighborhood name with 0 as value."""
    neighbourhoods_dict = {}
    for neighborhood in get_neighborhoods():
        neighbourhoods_dict[neighborhood] = 0
    return neighbourhoods_dict

def get_neighborhood_dict_array():
    """returns dictionary with each neighborhood name with array as value."""
    neighbourhoods_dict = {}
    for neighbourhood in get_neighborhoods():
        neighbourhoods_dict[neighbourhood] = [0, 0]
    return neighbourhoods_dict

def get_neighborhood_count():
    """returns a dictionary of the neighborhoods and the number of listings."""
    neighbourhoods = get_neighborhood_dict()
    with open('data/listings.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            neighbourhoods[row['neighbourhood_cleansed']] += 1
    return neighbourhoods

def get_rating_types():
    """returns array with all the neighborhood names."""
    return ['review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness',\
        'review_scores_checkin', 'review_scores_communication', 'review_scores_location', \
        'review_scores_value']

def get_most_positive_reviews(rating_type):
    """returns a sorted list of arrays of each neighborhood and their rating
        average based on the rating type."""
    with open('data/listings.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        neighborhoods = get_neighborhood_dict_array()
        row_rates = get_rating_types()
        max_ratings = []
        if not rating_type in row_rates:
            return max_ratings
        for row in reader:
            if not row[rating_type] == '':
                neighborhoods[row['neighbourhood_cleansed']][0] += 1
                neighborhoods[row['neighbourhood_cleansed']][1] += int(row[rating_type])
        for neighborhood, ratings in neighborhoods.items():
            rating_avg = ratings[1] / float(ratings[0])
            max_ratings.append([neighborhood, rating_avg])
        max_ratings.sort(key=itemgetter(1), reverse=True)
        return max_ratings
def get_overall_reviews():
    ratings = get_neighborhood_dict()
    for rating_type in get_rating_types():
        for rate in get_most_positive_reviews(rating_type):
            ratings[rate[0]] += rate[1]
    for k, val in ratings.items():
        ratings[k] = float(val / 7)
    return sorted(ratings.items(), key=itemgetter(1), reverse=True)

def get_listing_id_from_location(latitude, longitude):
    with open('data/listings.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row['latitude'] == latitude) and (row['longitude'] == longitude):
                return row['id']
        return -1

def get_ids():
    ctr = 0
    with open('data/listings.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if ctr == 30:
                return
            else:
                print row['latitude'], ',', row['longitude']
                ctr += 1



def get_occupancy_rate(listing_id):
    """total number of dates booked divided the total number of days avaliable."""
    with open('data/calendar.csv') as csvfile:
        found = False
        avaliability = [0, 0] # a[0] = booked, a[1] = not booked
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['listing_id'] == listing_id:
                if not found:
                    found = True
                if row['available'] == 'f':
                    avaliability[1] += 1
                else:
                    avaliability[0] += 1
            else:
                if found:
                    break
                else:
                    continue
        return avaliability[0] / float(avaliability[0] + avaliability[1])
print get_occupancy_rate(get_listing_id_from_location('37.751992462976204', '-122.40421045324041'))