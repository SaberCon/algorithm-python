class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return "0"
        plus = num > 0
        num = abs(num)
        ans = ""
        while num:
            ans = str(num % 7) + ans
            num //= 7
        return ans if plus else "-" + ans

