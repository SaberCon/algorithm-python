class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        N = len(nums)
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)
        ans = max_first = max_second = 0
        for i in range(N):
            max_first = max(max_first, sums[i] - sums[max(0, i - firstLen)])
            max_second = max(max_second, sums[i] - sums[max(0, i - secondLen)])
            ans = max(ans, max_first + sums[min(N, i + secondLen)] - sums[i])
            ans = max(ans, max_second + sums[min(N, i + firstLen)] - sums[i])
        return ans
