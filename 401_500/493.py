class Solution:
    def reversePairs(self, nums: [int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        bit = [0] * (len(nums) + 1)

        def bit_add(n):
            while n < len(bit):
                bit[n] += 1
                n += n & -n

        def bit_get(n):
            ans = 0
            while n > 0:
                ans += bit[n]
                n -= n & -n
            return ans

        def binary_search(left, right, num):
            if left == right - 1:
                return left if sorted_nums[left] >= num else -1
            mid = (left + right) // 2
            if sorted_nums[mid] >= num:
                return binary_search(mid, right, num)
            else:
                return binary_search(left, mid, num)

        count = 0
        for num in nums:
            count += bit_get(binary_search(0, len(nums), 2 * num + 1) + 1)
            bit_add(binary_search(0, len(nums), num) + 1)
        return count