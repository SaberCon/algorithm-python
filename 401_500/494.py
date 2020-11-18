class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sum_count = {0: 1}
        for num in nums:
            new_sum_count = {}
            for sum, count in sum_count.items():
                new_sum_count[sum + num] = new_sum_count.get(sum + num, 0) + count
                new_sum_count[sum - num] = new_sum_count.get(sum - num, 0) + count
            sum_count = new_sum_count
        return sum_count.get(S, 0)
