def generate_affiliation_link(url):
    # print(url[url.rfind('/dp')::])
    return 'http://www.amazon.com'+url[url.rfind('/dp')::]


# print(generate_affiliation_link('http://www.amazon.com/dp/1936891026/?tag=pyb0f-20'))