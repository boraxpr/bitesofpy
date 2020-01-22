import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies = defaultdict(list)
    with open(MOVIE_DATA, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Some movies do not have title_year data
            if len(row['title_year']) != 0:
                title_year = int(row['title_year'])
            movie = Movie(row['movie_title'].replace('\xa0', ''), title_year, float(row['imdb_score']))
            director = row['director_name']
            if title_year < MIN_YEAR:
                continue
            movies[director].append(movie)
    return movies


# print(get_movies_by_director())
def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    score = 0
    for movie in movies:
        score += movie.score
    return round(score / len(movies), ndigits=1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    score_entry = namedtuple('score_entry', 'director mean')
    result = list()
    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            scores = list(map(lambda x: x.score, movies))
            mean = round(sum(scores) / len(scores),ndigits=1)
            result.append(score_entry(director, mean))
    result.sort(key=lambda x: x.mean, reverse=-1)
    return result
