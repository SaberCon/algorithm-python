class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        nums = [a, b, c]
        ans = []
        while sum(n == 0 or (len(ans) > 1 and ans[-1] == i and ans[-2] == i) for i, n in enumerate(nums)) < 3:
            rank = sorted(range(3), key=lambda i: nums[i], reverse=True)
            choice = rank[1] if len(ans) > 1 and ans[-1] == rank[0] and ans[-2] == rank[0] else rank[0]
            ans.append(choice)
            nums[choice] -= 1
        return ''.join(chr(ord('a') + i) for i in ans)
