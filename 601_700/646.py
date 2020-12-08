class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda p: p[1])
        ans = 0
        curr = pairs[0][0] - 1
        for start, end in pairs:
            if start > curr:
                curr = end
                ans += 1
        return ans
