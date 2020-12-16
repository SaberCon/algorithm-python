class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        ADD, MULTIPLY, SUBTRACT, DIVIDE = 0, 1, 2, 3

        def solve(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i == j:
                        continue
                    new_nums = []
                    for k, z in enumerate(nums):
                        if k != i and k != j:
                            new_nums.append(z)
                    for k in range(4):
                        if k < 2 and i > j:
                            continue
                        if k == ADD:
                            if i > j:
                                continue
                            new_nums.append(x + y)
                        elif k == MULTIPLY:
                            if i > j:
                                continue
                            new_nums.append(x * y)
                        elif k == SUBTRACT:
                            new_nums.append(x - y)
                        elif k == DIVIDE:
                            if abs(y) < 1e-6:
                                continue
                            new_nums.append(x / y)
                        if solve(new_nums):
                            return True
                        new_nums.pop()
            return False

        return solve(nums)
