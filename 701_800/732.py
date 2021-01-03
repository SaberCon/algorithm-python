from bisect import bisect_left


class MyCalendarThree:

    def __init__(self):
        self.counts = [[-1, 0], [10 ** 9 + 1, 0]]

    def book(self, start: int, end: int) -> int:
        si = bisect_left(self.counts, [start, 0])
        if self.counts[si] == start:
            self.counts[si][1] += 1
        else:
            self.counts.insert(si, [start, 1])
        ei = bisect_left(self.counts, [end, 0])
        if self.counts[ei] == end:
            self.counts[ei][1] -= 1
        else:
            self.counts.insert(ei, [end, -1])
        ans = curr = 0
        for _, count in self.counts:
            curr += count
            ans = max(ans, curr)
        return ans
