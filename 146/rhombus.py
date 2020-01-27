STAR = '*'


def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """

    for rowz in range(1, (width * 2) + 1, 2):
        if rowz-width <= 0:
            yield '{:^{width}}'.format(STAR * rowz, width=width)
        else:
            multiplierOf4 = (rowz-width)//2
            yield '{:^{width}}'.format(STAR * (rowz-4*multiplierOf4), width=width)

gen = gen_rhombus(5)
for row in gen:
    print(row)
