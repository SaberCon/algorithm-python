class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        N = len(words)

        overlaps = [[0] * N for _ in range(N)]
        for i, x in enumerate(words):
            for j, y in enumerate(words):
                for ans in range(min(len(x), len(y)), 0, -1):
                    if x.endswith(y[:ans]):
                        overlaps[i][j] = ans
                        break

        dp = [[0] * N for _ in range(1 << N)]
        parent = [[-1] * N for _ in range(1 << N)]
        for mask in range(1, 1 << N):
            for bit in range(N):
                if (mask >> bit) & 1 == 0:
                    continue
                pmask = mask ^ (1 << bit)
                for i in range(N):
                    if (pmask >> i) & 1 == 0:
                        continue
                    value = dp[pmask][i] + overlaps[i][bit]
                    if value > dp[mask][bit] or dp[mask][bit] == 0:
                        dp[mask][bit] = value
                        parent[mask][bit] = i

        perm = []
        mask = (1 << N) - 1
        i = max(range(N), key=lambda n: dp[-1][n])
        for _ in range(N):
            perm.append(i)
            mask, i = mask ^ (1 << i), parent[mask][i]

        perm = perm[::-1]
        ans = [words[perm[0]]]
        for curr, last in zip(perm[1:], perm):
            ans.append(words[curr][overlaps[last][curr]:])

        return "".join(ans)
