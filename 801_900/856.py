class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for c in S:
            if c == '(':
                stack.append(0)
            else:
                total = 0
                while stack[-1] != 0:
                    total += stack.pop()
                stack[-1] = total * 2 if total else 1
        return sum(stack)
