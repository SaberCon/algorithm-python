class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        prev = matrix[0][1:]
        for row in matrix:
            if row[1:] != prev:
                return False
            prev = row[:-1]
        return True
