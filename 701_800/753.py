class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return ''.join(str(i) for i in range(k))
        chars = [str(i) for i in range(k - 1, -1, -1)]
        ans = '0' * (n - 1)
        used = set()
        for _ in range(k ** n):
            for c in chars:
                curr = ans[1 - n:] + c
                if ans[1 - n:] + c in used:
                    continue
                used.add(curr)
                ans += c
                break
        return ans
