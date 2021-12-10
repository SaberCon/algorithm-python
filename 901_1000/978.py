class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = cur = 1
        for i in range(1, len(arr)):
            if i > 1 and (arr[i] - arr[i - 1]) * (arr[i - 1] - arr[i - 2]) < 0:
                cur += 1
            else:
                cur = 1 + ((arr[i] - arr[i - 1]) == 0)
            ans = max(ans, cur)
        return ans
