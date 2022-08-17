class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        arr = [-1] * 32
        ans = mask = 0
        for i, c in enumerate(s):
            v = 'aeiou'.find(c)
            if v >= 0:
                mask ^= 1 << v
                if mask and arr[mask] < 0:
                    arr[mask] = i
            ans = max(ans, i - arr[mask])
        return ans
