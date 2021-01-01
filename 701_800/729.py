from bisect import bisect_left


class MyCalendar:

    def __init__(self):
        self.calendar = [(-1, -1), (10 ** 9 + 1, 10 ** 9 + 1)]

    def book(self, start: int, end: int) -> bool:
        index = bisect_left(self.calendar, (start, end))
        if self.calendar[index - 1][1] > start or self.calendar[index][0] < end:
            return False
        self.calendar.insert(index, (start, end))
        return True
