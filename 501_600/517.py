class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        if total % len(machines):
            return -1
        average = total // len(machines)

        curr_sum = max_sum = ans = 0
        for m in machines:
            curr_sum += m - average
            max_sum = max(max_sum, abs(curr_sum))
            ans = max(ans, max_sum, m - average)
        return ans
