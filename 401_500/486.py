class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        cache = {}

        def max_score(left, right):
            if left > right:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]
            left_score = nums[left] + min(max_score(left + 2, right), max_score(left + 1, right - 1))
            right_score = nums[right] + min(max_score(left + 1, right - 1), max_score(left, right - 2))
            cache[(left, right)] = max(left_score, right_score)
            return cache[(left, right)]

        return max_score(0, len(nums) - 1) >= (sum(nums) + 1) // 2
