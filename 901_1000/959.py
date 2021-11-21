class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        seen = set()
        ans = 0

        def cover(i, j, d):
            if i < 0 or i >= N or j < 0 or j >= N or (i, j, d) in seen:
                return
            if grid[i][j] == ' ':
                seen.add((i, j, 't'))
                seen.add((i, j, 'b'))
                seen.add((i, j, 'l'))
                seen.add((i, j, 'r'))
                for ni, nj, nd in ((i + 1, j, 't'), (i - 1, j, 'b'), (i, j + 1, 'l'), (i, j - 1, 'r')):
                    cover(ni, nj, nd)
            if grid[i][j] == '/':
                if d == 't' or d == 'l':
                    seen.add((i, j, 't'))
                    seen.add((i, j, 'l'))
                    for ni, nj, nd in ((i - 1, j, 'b'), (i, j - 1, 'r')):
                        cover(ni, nj, nd)
                else:
                    seen.add((i, j, 'b'))
                    seen.add((i, j, 'r'))
                    for ni, nj, nd in ((i + 1, j, 't'), (i, j + 1, 'l')):
                        cover(ni, nj, nd)
            if grid[i][j] == '\\':
                if d == 't' or d == 'r':
                    seen.add((i, j, 't'))
                    seen.add((i, j, 'r'))
                    for ni, nj, nd in ((i - 1, j, 'b'), (i, j + 1, 'l')):
                        cover(ni, nj, nd)
                else:
                    seen.add((i, j, 'b'))
                    seen.add((i, j, 'l'))
                    for ni, nj, nd in ((i + 1, j, 't'), (i, j - 1, 'r')):
                        cover(ni, nj, nd)

        for i in range(N):
            for j in range(N):
                for d in ('t', 'b', 'l', 'r'):
                    if (i, j, d) not in seen:
                        ans += 1
                        cover(i, j, d)
        return ans
