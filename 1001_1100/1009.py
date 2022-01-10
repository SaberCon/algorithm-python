class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return n ^ ((1 << len(bin(n)[2:])) - 1)
