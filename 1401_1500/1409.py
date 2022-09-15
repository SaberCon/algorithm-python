from collections import deque
from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        ans = []
        p = deque(range(1, m + 1))
        for q in queries:
            ans.append(p.index(q))
            p.remove(q)
            p.appendleft(q)
        return ans
