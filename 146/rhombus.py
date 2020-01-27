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
    print_row = lambda i,width: f'{STAR*i: ^{width}}'
    for i in range(1, width+1, 2):
        yield print_row(i, width)
    for i in range(width-2, 0, -2):
        yield print_row(i, width)