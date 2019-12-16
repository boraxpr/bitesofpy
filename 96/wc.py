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
    char_counter = 1
    for line in data.splitlines():
        # print(ch)
        line_counter = line_counter+1
        for word in line.split(" "):
            if word is not None:
                word_counter = word_counter+1
            for char in word:
                # print(char)
                char_counter = char_counter+1

    return str(line_counter) + "\t" + str(word_counter)+ "\t" + str(char_counter) + "\t" + file_

if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))