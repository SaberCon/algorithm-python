class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width = int(area ** 0.5)
        while True:
            if area % width == 0:
                return [area // width, width]
            width -= 1
