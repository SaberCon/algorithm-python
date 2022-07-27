from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        nums = defaultdict(set)
        for i, n in enumerate(arr):
            nums[n].add(i)
        nums[arr[0]].remove(0)
        queue = deque(((0, 0),))
        while queue:
            i, count = queue.popleft()
            if i == len(arr) - 1:
                return count
            for j in (i - 1, i + 1):
                if 0 <= j < len(arr) and j in nums[arr[j]]:
                    nums[arr[j]].remove(j)
                    queue.append((j, count + 1))
            queue.extend((j, count + 1) for j in nums[arr[i]])
            nums[arr[i]].clear()
        raise AssertionError()
