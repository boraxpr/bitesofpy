def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    means = list()
    tot = 0
    for id, val in enumerate(sequence):
        tot += val
        id += 1
        # print(str(id)+' '+str(val)+' '+str(tot))
        mean = tot/id
        mean = mean.__round__(2)
        means.append(mean)
    return means


# print(running_mean([1, 2, 3, 4, 5, 7.1]))