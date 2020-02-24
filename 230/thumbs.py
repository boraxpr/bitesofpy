THUMBS_UP, THUMBS_DOWN = '👍', '👎'


def emoji_multiply(multiplier):
    if multiplier == 0:
        raise ValueError("Specify a number")
    thumb = THUMBS_UP if multiplier > 0 else THUMBS_DOWN
    multiplier = abs(multiplier)
    return f"{thumb} ({multiplier}x)" if multiplier > 3 else thumb*multiplier


class Thumbs:
    def __mul__(self, multiplier):
        return emoji_multiply(multiplier)

    def __rmul__(self, multiplier):
        return self.__mul__(multiplier)