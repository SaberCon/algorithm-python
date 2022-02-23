class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        while str1 != str2:
            str1, str2 = sorted((str1, str2), key=len)
            if not str2.startswith(str1):
                return ''
            str2 = str2[len(str1):]
        return str1
