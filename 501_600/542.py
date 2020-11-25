class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        height, width = len(matrix), len(matrix[0])

        def update(x, y, distance):
            if x < 0 or x >= height or y < 0 or y >= width:
                return
            if distance != 0 and matrix[x][y] != -1 and matrix[x][y] <= distance:
                return
            matrix[x][y] = distance
            for dx, dy in ((0, 1), (1, 0)):
                update(x + dx, y + dy, distance + 1)

        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 1:
                    matrix[i][j] = -1
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    update(i, j, 0)
        return matrix