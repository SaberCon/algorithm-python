from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        total = sum(arr[:k])
        ans = total >= threshold
        for i in range(len(arr) - k):
            total += arr[i + k] - arr[i]
            ans += total >= threshold
        return int(ans)
