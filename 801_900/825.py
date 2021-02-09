class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counts = [0] * 121
        for age in ages:
            counts[age] += 1
        ans = 0
        for age1, count1 in enumerate(counts):
            if count1 == 0:
                continue
            for age2, count2 in enumerate(counts):
                if age2 <= 0.5 * age1 + 7:
                    continue
                if age2 > age1:
                    break
                ans += count1 * count2
                if age1 == age2:
                    ans -= count1
        return ans
