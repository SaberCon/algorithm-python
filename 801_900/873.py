from collections import defaultdict


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        counts = defaultdict(lambda: 2)
        visited = set()
        ans = 0
        for i, num in enumerate(arr):
            for j in range(i):
                if arr[j] >= (num + 1) // 2:
                    break
                if num - arr[j] in visited:
                    counts[(num - arr[j], num)] = counts[(arr[j], num - arr[j])] + 1
                    ans = max(ans, counts[(num - arr[j], num)])
            visited.add(num)
        return ans
