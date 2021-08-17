import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        demand_quality = sorted((w / q, q) for q, w in zip(quality, wage))
        ans = total_quality = 0
        min_qualities = []
        for demand, quality in demand_quality:
            if len(min_qualities) < k:
                heapq.heappush(min_qualities, -quality)
                total_quality += quality
                ans = demand * total_quality
                continue
            if quality < -min_qualities[0]:
                total_quality += heapq.heappop(min_qualities) + quality
                heapq.heappush(min_qualities, -quality)
                ans = min(ans, demand * total_quality)
        return ans
