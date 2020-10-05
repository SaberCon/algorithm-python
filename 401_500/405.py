class Solution:
    def toHex(self, num: int) -> str:
        num_to_hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        num &= 0xffffffff
        result = ''
        while num:
            result = num_to_hex[15 & num] + result
            num >>= 4
        return result or '0'
