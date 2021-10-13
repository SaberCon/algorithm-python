from collections import deque


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        N = len(nums)
        nums = nums * 2
        queue = deque([(0, -1)])
        ans = -100000
        cur = 0
        for i, n in enumerate(nums):
            cur += n
            if (i - queue[0][1]) > N:
                queue.popleft()
            ans = max(ans, cur - queue[0][0])
            while queue and queue[-1][0] >= cur:
                queue.pop()
            queue.append((cur, i))
        return ans
