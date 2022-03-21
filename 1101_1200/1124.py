class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        stack = [(-1, 0)]
        ans = index = performance = 0
        for i, h in enumerate(hours):
            performance += 1 if h > 8 else -1
            if index > 0 and performance - stack[index - 1][1] > 0:
                index -= 1
            if index < len(stack) and performance - stack[index][1] <= 0:
                index += 1
            if index < len(stack):
                ans = max(ans, i - stack[index][0])
            if performance < stack[-1][1]:
                stack.append((i, performance))
        return ans
