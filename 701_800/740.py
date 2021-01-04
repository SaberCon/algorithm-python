from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = sorted(Counter(nums).items())
        dp = [0]
        for i, (point, count) in enumerate(points):
            dp.append(max(dp[-1], point * count + (dp[-1] if i == 0 or (point - 1) > points[i - 1][0] else dp[-2])))
        return dp[-1]
