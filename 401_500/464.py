class Solution:
    def __init__(self):
        self.cache = {}

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (maxChoosableInteger + 1) * maxChoosableInteger // 2 < desiredTotal:
            return False
        return self.can_i_win(list(range(1, maxChoosableInteger + 1)), desiredTotal)

    def can_i_win(self, nums: [], desiredTotal: int) -> bool:
        if nums[-1] >= desiredTotal:
            return True
        key = (*nums, -desiredTotal)
        if key in self.cache:
            return self.cache[key]
        for i in range(len(nums)):
            num = nums[i]
            del nums[i]
            lose = self.can_i_win(nums, desiredTotal - num)
            nums.insert(i, num)
            if not lose:
                self.cache[key] = True
                return True
        self.cache[key] = False
        return False
