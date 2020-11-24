class Solution:
    def reversePairs(self, nums: [int]) -> int:
        def merge_sort(start, end):
            if start >= end:
                return 0
            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid + 1, end)

            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    count += mid - i + 1
                    j += 1

            left, right = nums[start:mid + 1], nums[mid + 1:end + 1]
            left_i, right_i = 0, 0
            for i in range(start, end + 1):
                if left_i >= len(left) or (right_i < len(right) and right[right_i] < left[left_i]):
                    nums[i] = right[right_i]
                    right_i += 1
                else:
                    nums[i] = left[left_i]
                    left_i += 1
            return count

        return merge_sort(0, len(nums) - 1)
