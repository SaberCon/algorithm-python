from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ps = [0] * (len(arr) + 1)
        for i, n in enumerate(arr):
            ps[i + 1] = ps[i] ^ n
        return [ps[right + 1] ^ ps[left] for left, right in queries]
