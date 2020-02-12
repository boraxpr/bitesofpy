import re

def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""
    regex = r"([a-zA-Z0-9\s\,]+[\?\.\!]*)"
    match = re.findall(regex,text)
    match = map(str.lstrip,list(match))
    match = map(str.capitalize,list(match))
    return " ".join(match)
