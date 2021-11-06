class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        indices = {n: i for i, n in enumerate(popped)}

        def check(pushed_i, popped_i, size):
            if size == 0:
                return True
            p = indices[pushed[pushed_i]]
            if p < popped_i or p >= popped_i + size:
                return False
            left, right = p - popped_i, size - (p - popped_i) - 1
            return check(pushed_i + 1, popped_i, left) and check(pushed_i + left + 1, p + 1, right)

        return check(0, 0, len(pushed))
