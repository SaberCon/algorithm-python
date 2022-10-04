from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        ps = [0] * (n + 1)
        for i, num in enumerate(arr):
            ps[i + 1] = ps[i] ^ num
        return sum(j - i for i in range(n - 1) for j in range(i + 1, n) if ps[j + 1] ^ ps[i] == 0)
