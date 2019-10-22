from collections import Counter
import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    listofautomaker = []
    makrset = set()
    countdict = dict()
    for item in data:
        itemyear = item['year']
        itemautomaker = item['automaker']
        # itemmodel = item['model']
        itemyear = item['year']

        if itemyear == year:
            listofautomaker.append(itemautomaker)
            makrset.add(itemautomaker)
    c = Counter(listofautomaker)
    # print(makrset)
    # print(listofautomaker)
    for each in makrset:
        countdict[each] = c[each]
        # print(each + ": " + c[each].__str__())
    sortx = sorted(countdict.items(), key=lambda x:x[1], reverse=True)
    dictkun = dict(sortx)
    return next(iter(dictkun))

def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    # cnt = Counter(row["automaker"] for row in data
    #               if row["year"] == year).most_common()
    modelset = set()
    for item in data:
        itemyear = item['year']
        itemautomaker = item['automaker']
        itemmodel = item['model']
        itemyear = item['year']

        if itemautomaker == automaker:
            if itemyear == year:
              modelset.add(itemmodel)
    # print(modelset)
    return modelset


# most_prolific_automaker(2008)
# print(most_prolific_automaker(2008))
# get_models('Volkswagen', 2008)