from collections import deque


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        sums = [0]
        for num in nums:
            sums += [sums[-1] + num]
        lows = deque()
        ans = len(sums)
        for i, s in enumerate(sums):
            while lows and s <= lows[-1][1]:
                lows.pop()
            target = s - k
            while lows and lows[0][1] <= target:
                ans = min(ans, (i - lows.popleft()[0]))
            lows.append((i, s))
        return ans if ans < len(sums) else -1
