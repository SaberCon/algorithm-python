from itertools import chain


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        return sum(min(duration, curr - prev) for curr, prev in zip(timeSeries, chain((-duration,), timeSeries)))
