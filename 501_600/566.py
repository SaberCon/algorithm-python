class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c:
            return nums
        ans = [[] for _ in range(r)]
        count = 0
        for row in nums:
            for num in row:
                ans[count // c].append(num)
                count += 1
        return ans
