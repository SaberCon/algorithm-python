class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        height, width = len(matrix), len(matrix[0])
        queue = []
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 1:
                    matrix[i][j] = -1
                else:
                    queue.append((i, j, 1))
        while queue:
            i, j, d = queue[0]
            del queue[0]
            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if 0 <= i + di < height and 0 <= j + dj < width and matrix[i + di][j + dj] == -1:
                    matrix[i + di][j + dj] = d
                    queue.append((i + di, j + dj, d + 1))
        return matrix
