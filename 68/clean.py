def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    o = ""
    for each in input_string:
        each = each.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
        o = o + each
    print(o)


# remove_punctuation("hello , !\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~world")

