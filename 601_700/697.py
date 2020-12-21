from collections import Counter


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        most_common = []
        degree = 0
        for num, count in Counter(nums).items():
            if count > degree:
                most_common = [num]
                degree = count
            elif count == degree:
                most_common.append(num)
        re_nums = nums.copy()
        re_nums.reverse()
        return min(len(nums) - re_nums.index(num) - nums.index(num) for num in most_common)
