import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        delays = defaultdict(list)
        for source, target, time in times:
            delays[source].append((target, time))
        visited = set()
        heap = [(0, K)]
        while heap:
            delay, target = heapq.heappop(heap)
            if target in visited:
                continue
            visited.add(target)
            if len(visited) == N:
                return delay
            for nex, time in delays[target]:
                heapq.heappush(heap, (delay + time, nex))
        return -1
