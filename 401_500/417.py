class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        a_set = set()
        p_set = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x: int, y: int, height: int, is_atlantic: bool):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if is_atlantic:
                current_set = a_set
            else:
                current_set = p_set
            if height > matrix[x][y] or (x, y) in current_set:
                return
            current_set.add((x, y))
            for direction in directions:
                dfs(x + direction[0], y + direction[1], matrix[x][y], is_atlantic)

        for i in range(n):
            dfs(0, i, 0, False)
            dfs(m - 1, i, 0, True)
        for i in range(m):
            dfs(i, 0, 0, False)
            dfs(i, n - 1, 0, True)
        return [key for key in a_set & p_set]
