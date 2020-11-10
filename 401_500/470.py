import random


def rand7():
    return random.randint(1, 7)


class Solution:
    def rand10(self):
        a, b = rand7(), rand7()
        while (a - 1) * 7 + b > 40:
            a, b = rand7(), rand7()
        return ((a - 1) * 7 + b - 1) // 4 + 1
