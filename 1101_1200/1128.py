from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = defaultdict(lambda: 0)
        for a, b in dominoes:
            counter[(min(a, b), max(a, b))] += 1
        return sum(v * (v - 1) // 2 for v in counter.values())
