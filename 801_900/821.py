class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        ans = [10000] * len(S)
        distance = 10000
        for i in range(len(S)):
            if S[i] == C:
                distance = 0
            ans[i] = min(ans[i], distance)
            distance += 1
        distance = 10000
        for i in range(len(S) - 1, -1, 0):
            if S[i] == C:
                distance = 0
            ans[i] = min(ans[i], distance)
            distance += 1
        return ans
