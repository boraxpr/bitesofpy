def generate_affiliation_link(url):
    # print(url[url.rfind('/dp')::])
    results = []
    for each in url:
        pos = each.rfind('/dp/')
        pos2 = each.rfind('/')
        # print(each[-1])
        link = 'http://www.amazon.com' + each[pos::]
        if link[-1] == 'X':
            link = link + '/?tag=pyb0f-20'
            results.append(link)
            continue
        else:
            link = 'http://www.amazon.com' + each[pos:pos2] + '/?tag=pyb0f-20'
            results.append(link)
    return results


print(generate_affiliation_link([
    ('https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/'
     '?keywords=war+of+art'),
    ('https://amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/'
     'ref=sr_1_1'),
    ('https://www.amazon.es/War-Art-Through-Creative-Battles/dp/1936891026/'
     '?qid=1537226234'),
     'https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X',
    ('https://www.amazon.com.au/Python-Cookbook-3e-David-Beazley/dp/'
     '1449340377/'),
    ('https://www.amazon.com/fake-book-with-longer-asin/dp/'
     '1449340377000/'),
]))