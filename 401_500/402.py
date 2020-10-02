class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num_stack = []

        for digit in num:
            while k and num_stack and num_stack[-1] > digit:
                num_stack.pop()
                k -= 1
            num_stack.append(digit)

        return ''.join(num_stack[:len(num_stack) - k]).lstrip('0') or '0'
