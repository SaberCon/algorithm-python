class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(counter):
            ans = 1
            for i, c in enumerate(counter):
                if c > 0:
                    counter[i] -= 1
                    ans += dfs(counter)
                    counter[i] += 1
            return ans

        counter = [0] * 26
        for t in tiles:
            counter[ord(t) - ord('A')] += 1
        return dfs([c for c in counter if c > 0]) - 1
