class Solution:
    def compress(self, chars: List[str]) -> int:
        curr = 0
        count = 1
        chars.append('end')
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                count += 1
            else:
                for n in chars[i - 1] + (str(count) if count != 1 else ''):
                    chars[curr] = n
                    curr += 1
                count = 1
        return curr
