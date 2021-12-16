class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = 'cc'
        while a > 0 or b > 0:
            if ans[-2:] == 'bb' or (ans[-2:] != 'aa' and a >= b):
                ans += 'a'
                a -= 1
            else:
                ans += 'b'
                b -= 1
        return ans[2:]
