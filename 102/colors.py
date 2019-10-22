VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check: 
       - if 'quit' was entered for color, print 'bye' and break. 
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    while True:
        inp = input()
        input_lowered = inp.lower()
        valid = 0
        if input_lowered == "quit":
            print("bye")
            break
        for color in VALID_COLORS:
            if color == input_lowered:
                valid = 1
        if valid == 1:
            print(input_lowered)
        else:
            print("Not a valid color")
            continue
        pass

print_colors()