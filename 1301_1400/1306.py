from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = {start}
        queue = deque(seen)
        while queue:
            i = queue.pop()
            if arr[i] == 0:
                return True
            for j in (i + arr[i], i - arr[i]):
                if 0 <= j < len(arr) and j not in seen:
                    queue.append(j)
                    seen.add(j)
        return False
