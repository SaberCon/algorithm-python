class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if k == 0:
            return [int(str(i) * n) for i in range(1, 10)]

        ans = []

        def backtracking(nums):
            if len(nums) == n:
                ans.append(int(''.join(map(str, nums))))
                return
            for i in (nums[-1] - k, nums[-1] + k):
                if 0 <= i < 10:
                    nums.append(i)
                    backtracking(nums)
                    nums.pop()

        for i in range(1, 10):
            backtracking([i])

        return ans
