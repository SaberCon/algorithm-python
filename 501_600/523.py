class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        curr_sum = 0
        sum_map = {0: -1}
        for i, num in enumerate(nums):
            curr_sum += num
            if k:
                curr_sum %= k
            if curr_sum in sum_map and i - sum_map[curr_sum] > 1:
                return True
            sum_map.setdefault(curr_sum, i)
        return False
