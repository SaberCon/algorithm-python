from functools import cache
from itertools import combinations
from typing import List


class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        target = (1 << n) - 1
        prerequisites = [0] * n
        for pre, nex in relations:
            prerequisites[nex - 1] |= 1 << (pre - 1)

        @cache
        def dp(prev: int) -> int:
            if prev == target:
                return 0
            courses = [i for i in range(n) if prev & (1 << i) == 0 and prev & prerequisites[i] == prerequisites[i]]
            return 1 + min(dp(prev | sum(1 << c for c in cs)) for cs in combinations(courses, min(k, len(courses))))

        return dp(0)
