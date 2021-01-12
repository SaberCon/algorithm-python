class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        return sum(s in jewels for s in stones)
