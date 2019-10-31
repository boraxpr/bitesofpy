def fizzbuzz(num):
    ret = []
    for each in num:
        if each % 3 == 0 and each % 5 == 0:
            ret.append('Fizz Buzz')
        elif each % 3 == 0:
            ret.append('Fizz')
        elif each % 5 == 0:
            ret.append('Buzz')
        else:
            ret.append(each)
    return ret

# print(fizzbuzz([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))