import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        heap = []
        speed_sum = 0
        ans = 0
        for e, s in sorted(zip(efficiency, speed), reverse=True):
            if len(heap) < k:
                heapq.heappush(heap, s)
                speed_sum += s
            else:
                speed_sum += s - heapq.heappushpop(heap, s)
            ans = max(ans, speed_sum * e)
        return ans % (10 ** 9 + 7)
