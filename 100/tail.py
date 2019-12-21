def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    file_ = str(filepath)
    for line in file_.split(" "):
        with open(file_, "r") as tempfile:
            data = tempfile.read()

    dat = list()
    for line in data.splitlines():
        dat.append(line)

    total_line = len(dat)
    # print(dat)
    dat = dat[total_line-n:total_line]
    # print(dat)
    return dat

