class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            ab, bb, cb = a & 1, b & 1, c & 1
            ans += not ab and not bb if cb else ab + bb
            a >>= 1
            b >>= 1
            c >>= 1
        return ans
