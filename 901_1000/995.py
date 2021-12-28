from collections import deque


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        ans = 0
        flip = 0
        queue = deque()
        for i, b in enumerate(nums):
            if queue and queue[0] <= i - k:
                queue.popleft()
                flip = flip ^ 1
            if b ^ flip:
                continue
            if i > len(nums) - k:
                return -1
            queue.append(i)
            flip = flip ^ 1
            ans += 1
        return ans
