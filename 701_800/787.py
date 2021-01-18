import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        flight_map = defaultdict(list)
        for s, d, p in flights:
            flight_map[s].append((d, p))
        heap = [(0, 0, src)]
        while heap:
            price, count, curr = heapq.heappop(heap)
            if curr == dst:
                return price
            if count > K:
                continue
            for d, p in flight_map[curr]:
                heapq.heappush(heap, (price + p, count + 1, d))
        return -1
