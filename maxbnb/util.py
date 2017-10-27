"""Methods for analyzing the data."""
import csv


def neighborhood_count():
    """returns a dictionary of the neighborhoods with the number of listings."""
    neighbourhoods = {}
    with open('data/neighbourhoods.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            neighbourhoods[row['neighbourhood']] = 0

    with open('data/listings.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            neighbourhoods[row['neighbourhood_cleansed']] += 1
    return neighbourhoods

"""for key, value in neighbourhoods.items():
    print(key, ': ', value)"""
