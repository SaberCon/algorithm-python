import heapq


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for i, num in enumerate(arr):
            heapq.heappush(heap, (num / arr[-1], i, len(arr) - 1))
        for _ in range(k - 1):
            _, i, j = heapq.heappop(heap)
            heapq.heappush(heap, (arr[i] / arr[j - 1], i, j - 1))
        _, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]
