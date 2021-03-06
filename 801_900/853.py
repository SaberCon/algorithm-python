class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = time = 0
        for p, s in sorted(zip(position, speed), reverse=True):
            t = (target - p) / s
            if t > time:
                ans += 1
                time = t
        return ans
