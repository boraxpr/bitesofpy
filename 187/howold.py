from dataclasses import dataclass

from dateutil import utils


@dataclass
class Actor:
    name: str
    born: str


@dataclass
class Movie:
    title: str
    release_date: str


def get_age(actor: Actor, movie: Movie) -> str:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    actor_born = utils.datetime.strptime(actor.born, "%B %d, %Y")
    movie_born = utils.datetime.strptime(movie.release_date, "%B %d, %Y")
    # actor_born = dateutil.utils.datetime.strptime()
    if actor_born.month < movie_born.month:
        year = movie_born.year-actor_born.year
    else:
        #By comparing year, we assume the end of the year
        year = movie_born.year-actor_born.year-1
    return f"{actor.name} was {year} years old when {movie.title} came out."

get_age(Actor('Wesley Snipes', 'July 31, 1962'),Movie('New Jack City', 'January 17, 1991'))