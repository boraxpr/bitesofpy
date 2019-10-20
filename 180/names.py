from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    # you code
    words=[]
    counter=0
    for line in data.split():
        for word in line.split(',', 2):
            words.append(word)
    words.remove('last_name')
    words.remove('first_name')
    words.remove('country_code')
    # print(words)
    for word in words:
        if len(word)==2:
            name = firstname + " " + lastname
            countries[word].append(name)
            continue
        if counter%2==0:
            lastname = word
            counter=1
            continue
        if counter%2==1:
            firstname = word
            counter=0
            continue
    return sorted(countries.items())




# print(group_names_by_country())