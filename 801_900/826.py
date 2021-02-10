class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort(reverse=True)
        profit_difficulty = sorted(zip(profit, difficulty), reverse=True)
        curr = ans = 0
        for w in worker:
            while profit_difficulty[curr][1] > w:
                curr += 1
                if curr >= len(profit_difficulty):
                    return ans
            ans += profit_difficulty[curr][0]
        return ans
