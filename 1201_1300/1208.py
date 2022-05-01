class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = [abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)]
        ans = 0
        current = 0
        j = -1
        for i in range(len(costs)):
            current += costs[i]
            while current > maxCost:
                j += 1
                current -= costs[j]
            ans = max(ans, i - j)
        return ans
