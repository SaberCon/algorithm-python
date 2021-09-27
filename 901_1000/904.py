class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        types = set()
        length = 0
        current = (-1, -1)
        for i, f in enumerate(fruits):
            if len(types) < 2 or f in types:
                types.add(f)
                length += 1
            else:
                ans = max(ans, length)
                types = {current[1], f}
                length = i - current[0] + 1
            if f != current[1]:
                current = (i, f)
        return max(ans, length)
