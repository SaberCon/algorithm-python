from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        start = -1
        total = 0
        ans = n + 1
        min_lengths = [n + 1] * (n + 1)
        for i, num in enumerate(arr):
            total += num
            while total > target:
                start += 1
                total -= arr[start]
            if total == target:
                length = i - start
                min_lengths[i + 1] = min(min_lengths[i], length)
                ans = min(ans, length + min_lengths[i + 1 - length])
            else:
                min_lengths[i + 1] = min_lengths[i]
        return ans if ans <= n else -1
