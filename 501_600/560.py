class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        sum_dict = {0: 1}
        ans = 0
        for num in nums:
            total += num
            if total - k in sum_dict:
                ans += sum_dict[total - k]
            sum_dict[total] = sum_dict.get(total, 0) + 1
        return ans
