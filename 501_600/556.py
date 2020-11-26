class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = [int(c) for c in str(n)]
        digits = []
        for num in nums[::-1]:
            if digits and digits[-1] > num:
                for i, digit in enumerate(digits):
                    if digit > num:
                        digits[i] = num
                        ans = int(''.join((str(d) for d in nums[:-len(digits) - 1] + [digit] + digits)))
                        return ans if ans <= 2 ** 31 else -1
            digits.append(num)
        return -1
