def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    tree = list()
    for row in range(rows):
        leaves = ((row+1)*2-1) * "*"
        tree.append(leaves.center((rows)*2))
    tree = "\n".join(tree)
    return tree

print(generate_xmas_tree())