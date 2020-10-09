import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        row, col = len(heightMap), len(heightMap[0])
        heap = []
        visited = set()
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        ans = 0

        def add_height(i, j, height=0):
            if (i, j) in visited:
                return
            heapq.heappush(heap, (height or heightMap[i][j], i, j))
            visited.add((i, j))

        # 初始为最外围的墙
        for i in range(row):
            add_height(i, 0)
            add_height(i, col - 1)
        for j in range(col):
            add_height(0, j)
            add_height(row - 1, j)
        # 从最小高度开始向内遍历
        while heap:
            height, i, j = heapq.heappop(heap)
            for di, dj in directions:
                tmp_i = i + di
                tmp_j = j + dj
                if tmp_i < 0 or tmp_j < 0 or tmp_i >= row or tmp_j >= col or (tmp_i, tmp_j) in visited:
                    continue
                if heightMap[tmp_i][tmp_j] < height:
                    ans += height - heightMap[tmp_i][tmp_j]
                    add_height(tmp_i, tmp_j, height)
                else:
                    add_height(tmp_i, tmp_j)
        return ans
