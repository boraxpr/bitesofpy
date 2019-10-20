import bisect


class OrderedList:

    def __init__(self):
        self._numbers = []

    def add(self, num):
        # you complete
        i = bisect.bisect_left(self._numbers, num)
        self._numbers.insert(i, num)

    def __str__(self):
        return ', '.join(str(num) for num in self._numbers)