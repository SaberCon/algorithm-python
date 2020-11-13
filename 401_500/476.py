class Solution:
    def findComplement(self, num: int) -> int:
        return (1 << (len(bin(num)) - 2)) - num - 1
