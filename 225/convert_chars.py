PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    result = ""
    for key,ch in enumerate(text):
        # print(text[key])
        if ch.lower() in PYBITES:
            if text[key].islower():
                # print(text[key])
                result += text[key].upper()
            elif text[key].isupper():
                # print(text[key])
                result += text[key].lower()
        else:
           result += text[key]
    return result
print(convert_pybites_chars("Elementum curabitur vitae nunc sed velit dignissim sodales ut."))