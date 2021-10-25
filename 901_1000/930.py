from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count_map = defaultdict(list)
        count_map[0].append(-1)
        count = 0
        ans = 0
        for i, n in enumerate(nums):
            if n == 1:
                count += 1
            ans += len(count_map[count - goal])
            count_map[count].append(i)
        return ans
