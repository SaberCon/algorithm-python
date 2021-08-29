import heapq


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []
        stops = 0
        for pos, fuel in stations + [(target, 0)]:
            while startFuel < pos:
                if not heap:
                    return -1
                startFuel -= heapq.heappop(heap)
                stops += 1
            heapq.heappush(heap, -fuel)
        return stops
