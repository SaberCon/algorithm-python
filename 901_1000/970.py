class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = set()
        px = 1
        while px < bound:
            py = 1
            while py <= bound - px:
                ans.add(px + py)
                py *= y
                if py == 1:
                    break
            px *= x
            if px == 1:
                break
        return list(ans)
