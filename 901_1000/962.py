import bisect


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = 0
        stack = []
        for i, n in enumerate(nums):
            if not stack or stack[-1][0] < -n:
                stack.append((-n, i))
                continue
            ans = max(ans, i - stack[bisect.bisect(stack, (-n, -1))][1])
        return ans
