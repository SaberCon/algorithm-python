class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        p_set = set()
        a_set = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x: int, y: int, height: int, o_set: set):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if height > matrix[x][y] or (x, y) in o_set:
                return
            o_set.add((x, y))
            for direction in directions:
                dfs(x + direction[0], y + direction[1], matrix[x][y], o_set)

        for i in range(n):
            dfs(0, i, 0, p_set)
            dfs(m - 1, i, 0, a_set)
        for i in range(m):
            dfs(i, 0, 0, p_set)
            dfs(i, n - 1, 0, a_set)
        return [key for key in a_set & p_set]
