class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_num = nums[0] if nums else 0
        ranges = []
        for num in nums:
            if num < min_num:
                min_num = num
            if num > min_num:
                while ranges:
                    if num <= ranges[-1][0]:
                        break
                    if num < ranges[-1][1]:
                        return True
                    ranges.pop()
                ranges.append((min_num, num))
        return False
