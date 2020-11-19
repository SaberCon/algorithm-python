class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        total = 0
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                total += i + num // i
                if i == num // i:
                    total -= i
        return total == 2 * num
