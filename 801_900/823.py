class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        mod = 10 ** 9 + 7
        nums = {n: i for i, n in enumerate(arr)}
        dp = [1] * len(arr)
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0 and arr[i] // arr[j] in nums:
                    dp[i] += dp[j] * dp[nums[arr[i] // arr[j]]]
        return sum(dp) % mod
