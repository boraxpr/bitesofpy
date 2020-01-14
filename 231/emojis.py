import re
from typing import List

# https://stackoverflow.com/a/43147265
# just for exercise sake, real life use emoji lib
IS_EMOJI = re.compile(r'[^\w\s,]')

def get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    eindices = list()
    for m in re.finditer(IS_EMOJI, text):
        eindices.append(m.start(0))
    return eindices

# print(get_emoji_indices('😂 ROFL that is funny 😂'))