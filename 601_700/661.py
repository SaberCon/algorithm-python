from statistics import mean


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        height, width = len(M), len(M[0])
        ans = [[0] * width for _ in range(height)]
        for i in range(height):
            for j in range(width):
                ans[i][j] = int(mean(M[i + a][j + b] for a in (-1, 0, 1) for b in (-1, 0, 1) if
                                 0 <= i + a < height and 0 <= j + b < width))
        return ans
