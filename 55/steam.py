from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "http://bit.ly/2IkFe9B"

Game = namedtuple('Game', 'title link')


def get_games():
    d = feedparser.parse(FEED_URL)
    list = []
    for num in range(len(d['entries'])):
        G = Game(d['entries'][num]['title'],d['entries'][num]['link'])
        list.append(G)

        # append(d['entries'][num]['link'])
        # print(d['entries'][num]['link'])
    return list
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""

# print(get_games())