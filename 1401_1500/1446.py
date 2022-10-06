class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        power = 1
        for c1, c2 in zip(s, s[1:]):
            if c1 == c2:
                power += 1
            else:
                power = 1
            ans = max(ans, power)
        return ans
