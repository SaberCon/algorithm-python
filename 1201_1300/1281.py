from functools import reduce
from operator import mul, add


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = [int(c) for c in str(n)]
        return reduce(mul, nums, 1) - reduce(add, nums, 0)
