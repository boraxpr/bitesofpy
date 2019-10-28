text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
vowels = 'aeiou'


def strip_vowels(text: str) -> (str, int):
    """Replace all vowels in the input text string by a star
       character (*).
       Return a tuple of (replaced_text, number_of_vowels_found)

       So if this function is called like:
       strip_vowels('hello world')

       ... it would return:
       ('h*ll* w*rld', 3)

       The str/int types in the function defintion above are part
       of Python's new type hinting:
       https://docs.python.org/3/library/typing.html"""
    listkun = list(text)
    count = 0
    for x in listkun:
        if x in vowels or x in "AEIOU":
            count+=1

    text = text.replace('a', '*')
    text = text.replace('e', '*')
    text = text.replace('i', '*')
    text = text.replace('o', '*')
    text = text.replace('u', '*')
    text = text.replace('A', '*')
    text = text.replace('E', '*')
    text = text.replace('I', '*')
    text = text.replace('O', '*')
    text = text.replace('U', '*')

    return (text, count)

# print(strip_vowels(text))
print(strip_vowels(text))