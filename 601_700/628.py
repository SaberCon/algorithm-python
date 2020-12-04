class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max3, min2 = [-10000, -10000, -10000], [10000, 10000]
        for num in nums:
            for i in range(len(max3)):
                if num > max3[i]:
                    for j in range(len(max3) - 1, i, -1):
                        max3[j] = max3[j - 1]
                    max3[i] = num
                    break
            if num < min2[0]:
                min2[0], min2[1] = num, min2[0]
            elif num < min2[1]:
                min2[1] = num
        return max(max3[0] * max3[1] * max3[2], max3[0] * min2[0] * min2[1])
