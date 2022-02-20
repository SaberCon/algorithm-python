class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        max_inc = inc = sum(grumpy[i] * customers[i] for i in range(minutes))
        for i in range(minutes, len(customers)):
            inc += grumpy[i] * customers[i] - grumpy[i - minutes] * customers[i - minutes]
            max_inc = max(max_inc, inc)
        return sum(c for c, g in zip(customers, grumpy) if g != 1) + max_inc
