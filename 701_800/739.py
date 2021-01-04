class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(T)
        for i, t in enumerate(T):
            while stack and stack[-1][0] < t:
                index = stack.pop()[1]
                ans[index] = i - index
            stack.append((t, i))
        return ans
