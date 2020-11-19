import heapq


class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        pc = [(-p, c) for p, c in zip(Profits, Capital)]
        heapq.heapify(pc)
        for i in range(min(k, len(pc))):
            temp = []
            p, c = heapq.heappop(pc)
            while c > W:
                if not pc:
                    return W
                temp.append((p, c))
                p, c = heapq.heappop(pc)
            W -= p
            for item in temp:
                heapq.heappush(pc, item)
        return W
