def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if rgb[0] > 255 or rgb[1] > 255 or rgb[2] > 255:
        raise ValueError
    return '#'+format(rgb[0],'02X') + format(rgb[1],'02X') + format(rgb[2],'02X')

# print(rgb_to_hex((255,255,0)))