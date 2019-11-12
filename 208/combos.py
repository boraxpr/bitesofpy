def find_number_pairs(numbers, N=10):
    result = []
    for number1 in numbers:
        for number2 in numbers:
            if number1+number2 == N and number1 != number2:
                tuple = (number1, number2)
                numbers.remove(number1)
                result.append(tuple)
    return result

# print(find_number_pairs([1,2,3,4,5,6,7]))