class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        perimeter = sum(nums)
        if not perimeter or perimeter % 4 != 0:
            return False
        lengths = [perimeter // 4] * 4
        nums.sort(reverse=True)

        def can_make_square(index):
            if index == len(nums):
                return sum(lengths) == 0
            for i in range(min(index + 1, 4)):
                if lengths[i] < nums[index]:
                    continue
                lengths[i] -= nums[index]
                if can_make_square(index + 1):
                    return True
                lengths[i] += nums[index]
            return False

        return can_make_square(0)
