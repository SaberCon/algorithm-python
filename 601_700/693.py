class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return bin(n ^ (n >> 1)).count('0') == 1
