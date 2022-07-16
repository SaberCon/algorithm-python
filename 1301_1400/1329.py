from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j, num in enumerate(sorted(mat[i + j][j] for j in range(min(m - i, n)))):
                mat[i + j][j] = num
        for i in range(1, n):
            for j, num in enumerate(sorted(mat[j][i + j] for j in range(min(m, n - i)))):
                mat[j][i + j] = num
        return mat
