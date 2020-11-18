class Solution:
    def reversePairs(self, nums: [int]) -> int:
        ans = 0
        for i in range(1, len(nums)):
            target = 2 * nums[i]
            left, right = 0, i - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
                    if left == right:
                        break
            ans += i - left
            curr = i
            while curr and nums[curr - 1] > nums[curr]:
                nums[curr], nums[curr - 1] = nums[curr - 1], nums[curr]
                curr -= 1
        return ans


# Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
print(Solution().reversePairs([1, 3, 2, 3, 1]))  # 2
print(Solution().reversePairs([2, 4, 3, 5, 1]))  # 3
