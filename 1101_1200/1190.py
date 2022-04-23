class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        pairs = {}
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            if c == ')':
                j = stack.pop()
                pairs[i], pairs[j] = j, i
        ans = []
        i = 0
        d = 1
        while i < len(s):
            if s[i] == '(' or s[i] == ')':
                i = pairs[i] - d
                d = -d
            else:
                ans.append(s[i])
                i += d
        return ''.join(ans)
