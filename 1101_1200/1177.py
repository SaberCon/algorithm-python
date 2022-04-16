class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        ps = [0] * (len(s) + 1)
        for i, c in enumerate(s):
            ps[i + 1] = ps[i] ^ (1 << (ord(c) - ord('a')))

        return [bin(ps[left] ^ ps[right + 1]).count('1') // 2 <= k for left, right, k in queries]
