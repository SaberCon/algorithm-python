class Solution:
    def findIntegers(self, num: int) -> int:
        bits = bin(num)[2:]
        last_0 = last_1 = 1
        flag = True
        for curr, last in zip(bits[1:], bits):
            if curr == '1' and last == '1':
                flag = False
            last_0, last_1 = last_0 + last_1, last_0 - 1 if flag and curr == '0' and last == '0' else last_0
        return last_0 + last_1
