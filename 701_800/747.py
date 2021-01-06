class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        top = second_top = index = -1
        for i, num in enumerate(nums):
            if num > top:
                index = i
                second_top = top
                top = num
            elif num > second_top:
                second_top = num
        return index if top >= 2 * second_top else -1
