class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)
        for i in range(len(sums) - 2):
            for j in range(i + 2, len(sums)):
                if (sums[j] - sums[i]) == k or (k != 0 and (sums[j] - sums[i]) % k == 0):
                    return True
        return False
