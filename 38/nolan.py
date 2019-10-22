import xml.etree.ElementTree as ET

# from OMDB
xmlstring = '''<?xml version="1.0" encoding="UTF-8"?>
<root response="True">
  <movie title="The Prestige" year="2006" rated="PG-13" released="20 Oct 2006" runtime="130 min" genre="Drama, Mystery, Sci-Fi" director="Christopher Nolan" />
  <movie title="The Dark Knight" year="2008" rated="PG-13" released="18 Jul 2008" runtime="152 min" genre="Action, Crime, Drama" director="Christopher Nolan" />
  <movie title="The Dark Knight Rises" year="2012" rated="PG-13" released="20 Jul 2012" runtime="164 min" genre="Action, Thriller" director="Christopher Nolan" />
  <movie title="Dunkirk" year="2017" rated="PG-13" released="21 Jul 2017" runtime="106 min" genre="Action, Drama, History" director="Christopher Nolan" />
  <movie title="Interstellar" year="2014" rated="PG-13" released="07 Nov 2014" runtime="169 min" genre="Adventure, Drama, Sci-Fi" director="Christopher Nolan"/>
</root>'''  # noqa E501


def get_tree():
    """You probably want to use ET.fromstring"""
    root = ET.fromstring(xmlstring)
    # for child in root:
    #     print(child.tag, child.attrib)
    return root


def get_movies():
    """Call get_tree and retrieve all movie titles, return a list or generator"""
    movies = []
    tree = get_tree()
    for child in tree:
        # print(child.attrib['title'])
        movies.append(child.attrib['title'])
    return movies


def get_movie_longest_runtime():
    """Call get_tree again and return the movie title for the movie with the longest
       runtime in minutes, for latter consider adding a _get_runtime helper"""
    runtime = dict()
    tree = get_tree()
    for child in tree:
        runtime[child.attrib['title']] = child.attrib['runtime']
    # print(runtime)
    sorted_runtime = sorted(runtime.items(), key=lambda x:x[1], reverse=True)
    # print(sorted_runtime[0][0])
    return sorted_runtime[0][0]

get_tree()
get_movies()
get_movie_longest_runtime()