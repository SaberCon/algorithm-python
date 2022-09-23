from collections import deque
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = deque()
        ans = -10000
        for i, num in enumerate(nums):
            if q and i - q[0][0] > k:
                q.popleft()
            s = num + q[0][1] if q and q[0][1] > 0 else num
            while q and q[-1][1] <= s:
                q.pop()
            q.append((i, s))
            ans = max(ans, s)
        return ans
