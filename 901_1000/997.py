class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judges = [True] * n
        for a, _ in trust:
            judges[a - 1] = False
        for i, b in enumerate(judges):
            if b:
                judge = i + 1
                break
        else:
            return -1
        return judge if sum(1 for _, b in trust if b == judge) == n - 1 else -1
