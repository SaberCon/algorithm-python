import heapq
from typing import List


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        target = [-num for num in target]
        heapq.heapify(target)
        while target[0] != -1:
            top = -heapq.heappop(target)
            other = total - top
            if not 0 < other < top:
                return False
            remainder = top % other if top % other else other
            heapq.heappush(target, -remainder)
            total -= top - remainder
        return True
