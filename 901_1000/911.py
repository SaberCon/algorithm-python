from bisect import bisect
from collections import Counter


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        counter = Counter()
        leading = 0
        self.leaders = []
        for person, time in zip(persons, times):
            counter[person] += 1
            if counter[person] >= leading:
                self.leaders.append((time, person))
                leading = counter[person]
            else:
                self.leaders.append((time, self.leaders[-1][1]))

    def q(self, t: int) -> int:
        i = bisect(self.leaders, (t, 10000))
        return self.leaders[i - 1][1]
