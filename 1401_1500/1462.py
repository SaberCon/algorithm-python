from functools import cache
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ps = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            ps[b].append(a)

        @cache
        def is_pre(u: int, v: int) -> bool:
            if u == v:
                return True
            return any(is_pre(u, p) for p in ps[v])

        return [is_pre(u, v) for u, v in queries]
