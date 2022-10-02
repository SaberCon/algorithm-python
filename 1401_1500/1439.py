import heapq
from typing import List


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        dp = [0]
        for row in mat:
            heap = []
            for r in row:
                for d in dp:
                    num = -(r + d)
                    if len(heap) < k:
                        heapq.heappush(heap, num)
                    elif num > heap[0]:
                        heapq.heappushpop(heap, num)
                    else:
                        break
            dp = sorted(-h for h in heap)
        return dp[-1]
