from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        froms = [[] for _ in range(n)]
        tos = [[] for _ in range(n)]
        for a, b in connections:
            tos[b].append(a)
            froms[a].append(b)
        ans = 0
        seen = set()
        queue = [0]
        while queue:
            city = queue.pop()
            seen.add(city)
            queue.extend(f for f in froms[city] if f not in seen)
            queue.extend(t for t in tos[city] if t not in seen)
            ans += sum(f not in seen for f in froms[city])
        return ans
