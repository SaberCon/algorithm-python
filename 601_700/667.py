class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        count = (k - 1) // 2
        ans = []
        s, e = 1, n
        while count:
            ans.append(s)
            ans.append(e)
            e -= 1
            s += 1
            count -= 1
        for i in range(s, e + 1):
            ans.append(i)
        if k % 2 == 0:
            ans[-1], ans[-2] = ans[-2], ans[-1]
        return ans
