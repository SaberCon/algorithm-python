class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = ls = 0
        for c in s:
            ls += 1 if c == 'L' else -1
            ans += ls == 0
        return ans
