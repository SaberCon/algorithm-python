class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = 0
        ans = 0
        for c in s:
            if c == '(':
                left += 1
            if c == ')':
                if left > 0:
                    left -= 1
                else:
                    ans += 1
        return ans + left
