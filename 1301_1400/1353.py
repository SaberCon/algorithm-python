import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.append([1000000, 1000000])
        heap = []
        day = 1
        ans = 0
        for start, end in sorted(events):
            while heap and start > day:
                if heapq.heappop(heap) >= day:
                    day += 1
                    ans += 1
            day = max(day, start)
            heapq.heappush(heap, end)
        return ans
