class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        curr = 0
        for i, num in enumerate(nums):
            if (total - num) % 2 == 0 and curr == (total - num) // 2:
                return i
            curr += num
        return -1
