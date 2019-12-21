def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    file_ = str(file_)
    for line in file_.split(" "):
        with open(file_, "r") as tempfile:
            data = tempfile.read()
    line_counter = 0
    word_counter = 0
    char_counter = 0
    for line in data.splitlines():
        # print(ch)
        # print(line)
        line_counter = line_counter+1
        # print(char_counter)
        for word in line.split():
            word_counter = word_counter+1
    char_counter = data.__len__()

    return str(line_counter) + " " + str(word_counter) + " " + str(char_counter) + " " + file_


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[0]))