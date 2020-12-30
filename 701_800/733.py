class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if newColor == oldColor:
            return image

        def fill(x, y):
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] != oldColor:
                return
            image[x][y] = newColor
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                fill(x + dx, y + dy)

        fill(sr, sc)
        return image
