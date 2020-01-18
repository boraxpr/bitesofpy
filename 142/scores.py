import numbers
from collections import namedtuple
from functools import reduce
from typing import List

MIN_SCORE = 4
DICE_VALUES = range(1, 7)

Player = namedtuple('Player', 'name scores')


def calculate_score(scores: List[int]) -> int:
    """Based on a list of score ints (dice roll), calculate the
       total score only taking into account >= MIN_SCORE
       (= eyes of the dice roll).

       If one of the scores is not a valid dice roll (1-6)
       raise a ValueError.

       Returns int of the sum of the scores.
    """
    #accumulated score
    acscore = 0
    for score in scores:
        if score not in DICE_VALUES:
            raise ValueError
        if score >= MIN_SCORE:
            acscore += score
    return acscore

def get_winner(players):
    """Given a list of Player namedtuples return the player
       with the highest score using calculate_score.

       If the length of the scores lists of the players passed in
       don't match up raise a ValueError.

       Returns a Player namedtuple of the winner.
       You can assume there is only one winner.

       For example - input:
         Player(name='player 1', scores=[1, 3, 2, 5])
         Player(name='player 2', scores=[1, 1, 1, 1])
         Player(name='player 3', scores=[4, 5, 1, 2])

       output:
         Player(name='player 3', scores=[4, 5, 1, 2])
    """
    lencheck = set()
    scores = dict()
    for player in players:
        lencheck.add(len(player.scores))
        if len(lencheck) > 1:
            raise ValueError
        scores.update({player.name: calculate_score(player.scores)})
    HighestscorePlayername = sorted(scores.items(),key=lambda x:x[1])[-1][0]
    for player in players:
        if player.name == HighestscorePlayername:
            return player

print(get_winner([
      Player(name='player 1', scores=[1, 3, 2, 5]),
      Player(name='player 2', scores=[1, 1, 1, 1]),
      Player(name='player 3', scores=[4, 5, 1, 2]),  # max 9
    ]))