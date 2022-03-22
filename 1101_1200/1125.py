class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        N = 1 << len(req_skills)
        dp = [None] * N
        dp[0] = tuple()
        for i, skills in enumerate(people):
            bits = sum(1 << j for j, s in enumerate(req_skills) if s in skills)
            for j in range(N - 1, -1, -1):
                k = j | bits
                if dp[j] is None or (dp[k] is not None and len(dp[k]) <= len(dp[j]) + 1):
                    continue
                dp[k] = dp[j] + (i,)
        return dp[-1]
