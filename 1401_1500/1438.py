from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dec, inc = deque(), deque()
        ans = 0
        i = -1
        for j, n in enumerate(nums):
            while dec and dec[-1][1] <= n:
                dec.pop()
            dec.append((j, n))
            while dec[0][1] > n + limit:
                i = dec.popleft()[0]
            while inc and inc[-1][1] >= n:
                inc.pop()
            inc.append((j, n))
            while inc[0][1] < n - limit:
                i = inc.popleft()[0]
            ans = max(ans, j - i)
        return ans
