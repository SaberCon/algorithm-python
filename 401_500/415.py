class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        length = max(len(num1), len(num2))
        num1 = num1[::-1].ljust(length, '0')
        num2 = num2[::-1].ljust(length, '0')
        carry = 0
        nums = []
        for n1, n2 in zip(num1, num2):
            num = int(n1) + int(n2) + carry
            nums.append(str(num % 10))
            carry = num // 10
        if carry:
            nums.append(str(carry))
        return ''.join(nums[::-1])
