class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        width, length = len(matrix), len(matrix[0])

        ans = []
        for i in range(width + length - 1):
            if i % 2 == 0:
                for j in range(max(0, i - width + 1), min(i + 1, length)):
                    ans.append(matrix[i - j][j])
            else:
                for j in range(max(0, i - length + 1), min(i + 1, width)):
                    ans.append(matrix[j][i - j])
        return ans
