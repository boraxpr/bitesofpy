import pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def athletes_most_medals(data=data):
    data = pd.read_csv(data)
    # x = data.head(5)
    Men_most = data[(data.Gender == "Men")]["Athlete"].value_counts()
    Women_most = data[(data.Gender == "Women")]["Athlete"].value_counts()
    return {Men_most.index[0]: Men_most.values[0], Women_most.index[0]: Women_most.values[0]}


# print(athletes_most_medals(data))
