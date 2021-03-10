from bisect import bisect_left

from bisect import insort_left


class ExamRoom:

    def __init__(self, N: int):
        self.seats = []
        self.size = N

    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0
        pos = distance = 0
        if self.seats[0] != 0:
            distance = self.seats[0]
            pos = 0
        for i in range(len(self.seats) - 1):
            if (self.seats[i + 1] - self.seats[i]) // 2 > distance:
                distance = (self.seats[i + 1] - self.seats[i]) // 2
                pos = self.seats[i] + distance
        if self.seats[-1] != self.size - 1 and self.size - 1 - self.seats[-1] > distance:
            pos = self.size - 1
        insort_left(self.seats, pos)
        return pos

    def leave(self, p: int) -> None:
        self.seats.pop(bisect_left(self.seats, p))
