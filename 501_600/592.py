from functools import reduce


def add(num1, num2):
    n = num1[0] * num2[1] + num2[0] * num1[1]
    d = num1[1] * num2[1]
    g = gcd(n, d)
    return [n // g, d // g]


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


class Solution:
    def fractionAddition(self, expression: str) -> str:
        if not expression:
            return '0/1'
        curr = ''
        nums = []
        for c in expression:
            if curr and (c == '+' or c == '-'):
                nums.append(curr)
                curr = ''
            curr += c
        nums.append(curr)
        return '/'.join(map(str, reduce(add, map(lambda s: [int(n) for n in s.split('/')], nums))))
