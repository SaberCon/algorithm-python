class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n = str(n)
        ans = sum(len(digits) ** i for i in range(1, len(n)))
        for i, d in enumerate(n):
            ans += sum(1 for digit in digits if digit < d) * (len(digits) ** (len(n) - 1 - i))
            if d not in digits:
                break
        else:
            ans += 1
        return ans
