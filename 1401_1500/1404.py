class Solution:
    def numSteps(self, s: str) -> int:
        carry = ans = 0
        for b in s[:0:-1]:
            carry += b == '1'
            if carry % 2:
                carry += 1
                ans += 1
            carry //= 2
            ans += 1
        return ans + carry
