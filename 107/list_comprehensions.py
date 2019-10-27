def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    numbers = [i for i in numbers if i!=0 and i%2==0 and i>0]
    return numbers

# filter_positive_even_numbers([0,1,2,3,4,5,6,7,8,9])
# print(filter_positive_even_numbers([0,1,2,3,4,5,6,7,8,9]))