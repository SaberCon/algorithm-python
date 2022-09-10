class Solution:
    def numSteps(self, s: str) -> int:
        carry = False
        ans = 0
        for b in s[:0:-1]:
            ans += 1 + (carry ^ (b == '1'))
            carry |= b == '1'
        return ans + carry
