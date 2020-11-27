class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        ans = 0
        for i in range(len(nums)):
            if i in visited:
                continue
            visited.add(i)
            n, l = i, 1
            while nums[n] != i:
                n = nums[n]
                visited.add(n)
                l += 1
            ans = max(ans, l)
        return ans
