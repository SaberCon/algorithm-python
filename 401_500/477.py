class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        counts = [[0, 0] for _ in range(30)]
        for num in nums:
            for i in range(30):
                counts[i][(num & (1 << i)) > 0] += 1
        return sum(count[0] * count[1] for count in counts)
