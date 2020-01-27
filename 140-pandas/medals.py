import pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def athletes_most_medals(data=data):
    df = pd.read_csv(data)
    # x = data.head(5)
    Men_most = df[(df.Gender == "Men")]["Athlete"].value_counts()
    Women_most = df[(df.Gender == "Women")]["Athlete"].value_counts()
    return {Men_most.index[0]: Men_most.values[0], Women_most.index[0]: Women_most.values[0]}