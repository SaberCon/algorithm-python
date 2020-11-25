class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == nums[mid - 1]:
                if mid % 2:
                    left = mid + 1
                else:
                    right = mid - 2
            elif nums[mid] == nums[mid + 1]:
                if mid % 2:
                    right = mid - 1
                else:
                    left = mid + 2
            else:
                return nums[mid]
        return nums[left]
