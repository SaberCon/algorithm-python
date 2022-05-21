from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        gaps = [0]
        for n in nums:
            if n % 2:
                gaps.append(0)
            else:
                gaps[-1] += 1
        ans = 0
        for i in range(k, len(gaps)):
            ans += (gaps[i - k] + 1) * (gaps[i] + 1)
        return ans
