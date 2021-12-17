class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        start = sum(n for n in nums if n % 2 == 0)
        ans = []
        for val, i in queries:
            if nums[i] % 2 == 1 and val % 2 == 1:
                start += nums[i] + val
            if nums[i] % 2 == 0 and val % 2 == 1:
                start -= nums[i]
            if nums[i] % 2 == 0 and val % 2 == 0:
                start += val
            nums[i] += val
            ans.append(start)
        return ans
