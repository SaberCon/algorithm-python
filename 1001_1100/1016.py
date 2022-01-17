class Solution:
    def queryString(self, s: str, n: int) -> bool:
        M = len(s)
        N = len(bin(n)) - 2
        nums = set()
        for i in range(M):
            if s[i] == '0':
                continue
            for j in range(i + 1, min(i + N, M) + 1):
                num = int(s[i:j], 2)
                if num <= n:
                    nums.add(num)
        return len(nums) == n
