class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        perimeter = sum(nums)
        if not perimeter or perimeter % 4 != 0:
            return False
        side_length = perimeter // 4
        memo = set()

        def recurse(mask):
            if mask in memo:
                return False
            total = sum(nums[i] for i in range(len(nums)) if not (mask & (1 << i)))
            if total == side_length * 3:
                return True
            for i in range(len(nums)):
                if mask & (1 << i) and nums[i] <= side_length - total % side_length and recurse(mask ^ (1 << i)):
                    return True
            memo.add(mask)
            return False

        return recurse((1 << len(nums)) - 1)
