class Solution:
    def maxScore(self, s: str) -> int:
        zeros, ones = 0, sum(c == '1' for c in s)
        ans = 0
        for c in s[:-1]:
            if c == '0':
                zeros += 1
            if c == '1':
                ones -= 1
            ans = max(ans, zeros + ones)
        return ans
