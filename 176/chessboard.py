WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    type1 = " #"
    type2 = "# "
    dim = int(size)
    halfdim = int(dim/2)
    for y in range(dim):
        if y % 2 == 0:
            print(type1*halfdim)
        else:
            print(type2*halfdim)

create_chessboard(4)

