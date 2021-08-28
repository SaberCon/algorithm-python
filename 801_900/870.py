class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = sorted((n, i) for i, n in enumerate(nums2))
        ans = {}
        s, e = 0, len(nums) - 1
        for n in sorted(nums1):
            if n > nums[s][0]:
                ans[nums[s][1]] = n
                s += 1
            else:
                ans[nums[e][1]] = n
                e -= 1
        return [ans[i] for i in range(len(nums))]
