def generate_affiliation_link(url):
    # print(url[url.rfind('/dp')::])
    pos = url.rfind('/dp/')
    pos2 = url.rfind('/')
        # print(each[-1])
    link = 'http://www.amazon.com' + url[pos::]
    if link[-1] == 'X':
        link = link + '/?tag=pyb0f-20'
        return link
    else:
        link = 'http://www.amazon.com' + url[pos:pos2] + '/?tag=pyb0f-20'
        return link


# print(generate_affiliation_link('https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/'))