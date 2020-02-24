THUMBS_UP, THUMBS_DOWN = '👍', '👎'


def emoji_multiply(multiplier):
    if multiplier == 0:
        raise ValueError("Specify a number")
    thumb = THUMBS_UP
    if multiplier < 0:
        thumb = THUMBS_DOWN
    multiplier = abs(multiplier)
    if multiplier in [1, 2, 3]:
        return thumb * multiplier
    else:
        return str(thumb) + " ({}x)".format(multiplier)


class Thumbs:
    def __mul__(self, multiplier):
        return emoji_multiply(multiplier)

    def __rmul__(self, multiplier):
        return emoji_multiply(multiplier)