class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        N = len(num)
        ans = []
        while len(ans) < N or k > 0:
            n = (num[-len(ans) - 1] if len(ans) < N else 0) + k % 10
            ans.append(n % 10)
            k = k // 10 + n // 10
        return ans[::-1]
