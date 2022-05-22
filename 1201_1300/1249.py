class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c == ')' and stack and stack[-1][1] == '(':
                stack.pop()
            elif c == '(' or c == ')':
                stack.append((i, c))
        removed = {i for i, c in stack}
        return ''.join(c for i, c in enumerate(s) if i not in removed)
