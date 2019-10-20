from os import path
import statistics as st
from urllib.request import urlretrieve


STATS = path.join('/tmp', 'testfiles_number_loc.txt')
if not path.isfile(STATS):
    urlretrieve('https://bit.ly/2Jp5CUt', STATS)

STATS_OUTPUT = """
Basic statistics:
- count     : {count:7d}
- min       : {min_:7d}
- max       : {max_:7d}
- mean      : {mean:7.2f}

Population variance:
- pstdev    : {pstdev:7.2f}
- pvariance : {pvariance:7.2f}

Estimated variance for sample:
- count     : {sample_count:7.2f}
- stdev     : {sample_stdev:7.2f}
- variance  : {sample_variance:7.2f}
"""

def get_all_line_counts(data: str = STATS) -> list:
    """Get all 186 line counts from the STATS file,
       returning a list of ints"""
    # TODO 1: get the 186 ints from downloaded STATS file
    listofints = []
    counts=0
    with open(data, 'r') as file:
        data = file.read()
    for line in data.split():
        if not line:
            break
        if len(line) > 5:
            continue
        number = int(line)
        listofints.append(number)
        counts += 1
        # print(line)
        # print(counts)
    return listofints


def create_stats_report(data=None):
    if data is None:
        # converting to a list in case a generator was returned
        data = list(get_all_line_counts())

    # taking a sample for the last section
    sample = list(data)[::2]
    # print(sample.__len__())
    # TODO 2: complete this dict, use data list and
    # for the last 3 sample_ variables, use sample list
    stats = dict(count=None,
                 min_=None,
                 max_=None,
                 mean=None,
                 pstdev=None,
                 pvariance=None,
                 sample_count=None,
                 sample_stdev=None,
                 sample_variance=None,
                 )
    # print(min(data))
    # print(type(data))
    stats['count'] = len(data)
    # print(data.__len__())
    stats['min_'] = min(data)
    # print(min(data))
    stats['max_'] = max(data)
    # print(max(data))
    stats['mean'] = st.mean(data)
    stats['pstdev'] = st.pstdev(data)
    stats['pvariance'] = st.pvariance(data)
    stats['sample_count'] = sample.__len__()
    stats['sample_stdev'] = st.stdev(sample)
    stats['sample_variance'] = st.variance(sample)
    return STATS_OUTPUT.format(**stats)

# print(get_all_line_counts())
# print(get_all_line_counts().__len__())
# create_stats_report()