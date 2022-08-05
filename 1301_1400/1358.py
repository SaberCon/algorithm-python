class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        arr = [-1] * 3
        ans = 0
        for i, c in enumerate(s):
            arr[ord(c) - ord('a')] = i
            ans += min(arr) + 1
        return ans
