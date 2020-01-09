import textwrap

INDENTS = 4
poem = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """


def print_hanging_indents(poem):
    lines = textwrap.dedent(poem).splitlines()
    count = 0
    for line in lines:
        if len(line) == 0:
            count = 1
        if count == 0:
            line = textwrap.indent(line, prefix=' '*INDENTS)
        if len(line) != 0:
            count = 0
        # print(count)
        if len(line) != 0:
            print(line)


print_hanging_indents(poem)