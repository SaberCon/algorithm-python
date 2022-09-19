class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (1 << (n - 1)):
            return ''
        ans = ''
        for i in range(n):
            for letter in 'abc':
                if ans and letter == ans[-1]:
                    continue
                num = 1 << (n - i - 1)
                if k <= num:
                    ans += letter
                    break
                k -= num
        return ans
